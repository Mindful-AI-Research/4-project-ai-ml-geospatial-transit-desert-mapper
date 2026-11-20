"""Prepare IBGE Census 2022 sectors for the Transit Desert Mapper.

Reads the statewide GeoPackage (never modified), keeps the São Paulo municipality
(CD_MUN == "3550308"), preserves all original columns, reprojects to EPSG:31983,
and writes a derived GeoPackage plus a JSON report to data/processed/.

Run from the repository root:
    python src/data/prepare_ibge.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sys
from pathlib import Path

import geopandas as gpd
from shapely.validation import explain_validity

LOG = logging.getLogger("prepare_ibge")
LAYER = "SP_setores_CD2022"
MUN_CODE = "3550308"
TARGET_CRS = "EPSG:31983"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, default=Path("data/raw/IBGE/SP_setores_CD2022.gpkg"))
    p.add_argument("--outdir", type=Path, default=Path("data/processed"))
    a = p.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    out_gpkg = a.outdir / "ibge_sectors_sao_paulo_epsg31983.gpkg"
    out_json = a.outdir / "ibge_sectors_sao_paulo_report.json"
    if not a.input.exists():
        LOG.error("Input not found: %s", a.input)
        return 1
    if out_gpkg.exists() or out_json.exists():
        LOG.error("Output exists; refusing to overwrite: %s / %s", out_gpkg, out_json)
        return 1
    a.outdir.mkdir(parents=True, exist_ok=True)

    src_hash = sha256(a.input)
    state = gpd.read_file(a.input, layer=LAYER)
    LOG.info("State rows: %d, CRS: %s", len(state), state.crs)
    src_crs = str(state.crs)
    mun = state[state["CD_MUN"] == MUN_CODE].copy()
    cols_original = list(state.columns)

    # Checks on the source geometry (no repair is applied).
    empty = int(mun.geometry.is_empty.sum() + mun.geometry.isna().sum())
    invalid_mask = ~mun.geometry.is_valid
    invalid = int(invalid_mask.sum())
    reasons: dict[str, int] = {}
    for g in mun.geometry[invalid_mask]:
        key = explain_validity(g).split("[")[0].strip()
        reasons[key] = reasons.get(key, 0) + 1

    proj = mun.to_crs(TARGET_CRS)
    assert list(proj.columns) == cols_original, "columns changed"
    proj.to_file(out_gpkg, layer="sectors_sao_paulo", driver="GPKG")

    v1 = proj["v0001"]
    report = {
        "source_file": str(a.input),
        "source_sha256": src_hash,
        "source_layer": LAYER,
        "source_crs": src_crs,
        "state_rows": int(len(state)),
        "filter": f"CD_MUN == '{MUN_CODE}'",
        "municipality_rows": int(len(proj)),
        "output_file": str(out_gpkg),
        "output_crs": str(proj.crs),
        "columns_preserved": len(cols_original),
        "cd_setor_unique": bool(proj["CD_SETOR"].is_unique),
        "empty_or_null_geometries": empty,
        "invalid_geometries_tested": True,
        "invalid_geometries": invalid,
        "invalid_reasons": reasons,
        "v0001_nulls": int(v1.isna().sum()),
        "v0001_sum": int(v1.sum()),
        "v0001_eq_0_sectors": int((v1 == 0).sum()),
        "geometry_repaired": False,
    }
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    LOG.info("Report: %s", json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
