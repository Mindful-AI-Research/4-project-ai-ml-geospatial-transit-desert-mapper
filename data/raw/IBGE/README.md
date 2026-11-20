# IBGE — Census 2022 Census Sectors

## Purpose

This dataset provides census-sector boundaries and population attributes
for the São Paulo Transit Desert Mapper project.

The source dataset covers São Paulo state. The analysis must select
São Paulo municipality before calculating sector-level indicators.

## Download

Locate the IBGE Census 2022 dataset asset on the project's Releases page:

[Project dataset releases](https://github.com/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases)

Alternatively, obtain the dataset from the official IBGE directory:

[IBGE — São Paulo census sectors with attributes](https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/malha_com_atributos/setores/gpkg/UF/SP/)

The acquisition walkthrough identified `SP_setores_CD2022.gpkg`
in the official directory. The archive in the release was listed on 2026-11-19 and contains this file.

## Expected local structure

Approved layout. The original archive is kept unchanged and only the GeoPackage is extracted:

    data/raw/IBGE/
    ├── SP_setores_CD2022.tar.gz                  (original release asset, unchanged)
    ├── SP_setores_CD2022.gpkg                    (extracted; pipeline read path)
    └── Dicionario_de_dados_malha_agregados.xlsx  (IBGE data dictionary)

Extract without overwriting an existing file:

    tar -xzk -f data/raw/IBGE/SP_setores_CD2022.tar.gz -C data/raw/IBGE SP_setores_CD2022.gpkg

The archive also contains a macOS metadata file (`._SP_setores_CD2022.gpkg`) that is not needed.
Release asset: `data-v1`, `SP_setores_CD2022.tar.gz` (90,006,177 bytes). Release assets are stored separately
from the Git source tree. Cloning the repository does not download them.

## Data dictionary

File: `data/raw/IBGE/Dicionario_de_dados_malha_agregados.xlsx` (sheets `Setor`, `Distrito`, `Subdistrito`, `Bairro`).
The `Setor` sheet applies to the sector layer used here.

| GeoPackage field | Dictionary (sheet `Setor`) |
|---|---|
| `v0001` | "Total de pessoas" |
| `v0002` | Total de Domicílios (DPPO + DPPV + DPPUO + DPIO + DCCM + DCSM) |
| `v0003` | Total de Domicílios Particulares (DPPO + DPPV + DPPUO + DPIO) |
| `v0004` | Total de Domicílios Coletivos (DCCM + DCSM) |
| `v0005` | Média de moradores em Domicílios Particulares Ocupados (Total pessoas em Domicílios Particulares Ocupados / DPPO + DPIO) |
| `v0006` | Percentual de Domicílios Particulares Ocupados Imputados (Total DPO imputados / Total DPO) |
| `v0007` | Total de Domicílios Particulares Ocupados (DPPO + DPIO) |

Verified on 2026-11-19: the GeoPackage fields are lowercase (`v0001` to `v0007`) and the dictionary uses uppercase
(`V0001` to `V0007`); they are matched by name ignoring case. The values are consistent with the definitions in the
checks listed in `assets/dataset-sources-and-downloads.md`. Name differences: dictionary `CD_SUBDIS` versus GeoPackage
`CD_SUBDIST`, dictionary `CD_SITUACAO` versus GeoPackage `CD_SIT`.

The dictionary gives the definition "Total de pessoas". It does not state a reference population concept
beyond that wording, and it does not document how zero values or suppression are handled. Do not assume either.
Use the term "pessoas" for `v0001`, as in the dictionary.

## Coordinate reference system

The source GeoPackage uses EPSG:4674 (SIRGAS 2000, geographic coordinates). Metric calculations (distance, buffers, areas)
must use a projected CRS: this project uses EPSG:31983 (SIRGAS 2000 / UTM zone 23S). The derived subset is written
already reprojected by `src/data/prepare_ibge.py` to `data/processed/ibge_sectors_sao_paulo_epsg31983.gpkg`
(27,301 sectors of municipality `3550308`; all original attribute columns preserved).

## Dates: reference, update and download are different things

| Date | Value | Status |
|---|---|---|
| Reference | Census 2022 | The exact census reference date is Desconhecido nos materiais fornecidos (not stated in the sources read) |
| IBGE publication or update of this file | Desconhecido nos materiais fornecidos | Not shown in the archive, the GeoPackage or the sources read |
| Local file timestamp inside the archive | 2026-11-08 14:27 | Timestamp of the owner's local copy; not an IBGE date |
| Upload to the project release `data-v1` | 2026-11-09 (API `created_at` 03:15:54Z) | From `releases.json` |
| Download for the review inspection | 2026-11-19 | Actual acquisition date of the inspected copy |

Do not infer one of these from another.

## Detailed validation

Full methods, results, sources and limitations: [`docs/data-validation.md`](../../../docs/data-validation.md).
Summary of what is verified: dictionary definition of `v0001` ("Total de pessoas"), field correspondence, internal
consistency of the household fields, no null `v0001`, 412 sectors with `v0001` = 0 ("população registrada igual a zero";
the dictionary does not document zero or suppression rules), 3 geometries with ring self-intersection (not repaired).
Pending: comparison with the IBGE primary total and its release.

## Validation before analysis

Before using the dataset:

1. Confirm that the download is complete and the file opens successfully.
2. Inspect available layers and their documentation.
3. Identify the census-sector identifier and municipality field.
4. Population variable: `v0001`, "Total de pessoas" per the data dictionary (see above).
5. Select São Paulo municipality using the verified municipality field.
6. Check missing or suppressed values; do not automatically replace
   missing population with zero.
7. Inspect the coordinate reference system and geometry validity.
8. Confirm that the sector identifiers are suitable for the intended joins.

Do not guess column names or treat the presence of a file as proof
that its contents have been validated.

## Data handling

- Preserve original downloads unchanged.
- Keep extraction outputs separate from the original archive.
- Save cleaned, filtered, or transformed datasets in `data/processed/`.
- Do not overwrite the statewide source with the municipal subset.
- Document the input path used by the pipeline.

## Temporal reference

Population refers to Census 2022.

Transport datasets may refer to a different period. Document this
temporal mismatch when interpreting access indicators.

## Provenance

Record:

- Official source URL.
- Release asset URL, when applicable.
- Original filename.
- Actual download date.
- Dataset reference year.
- Extracted layers and selected population variable.
- License and attribution requirements.
- File checksum, when calculated.

## Attribution

Source: Instituto Brasileiro de Geografia e Estatística (IBGE),
Censo Demográfico 2022.

Consult the original dataset documentation for usage and attribution terms.
The repository's software license does not replace the source dataset's terms.
