# São Paulo Transit Desert Mapper — Dataset Sources and Downloads

## Overview

This document catalogs the datasets used by the São Paulo Transit
Desert Mapper and explains where to obtain them and where to store
them locally.

Project repository:
https://github.com/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper

Dataset releases:
https://github.com/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases

Large datasets are distributed through GitHub Releases or their
official sources rather than stored in the Git source tree.

Cloning the repository does not automatically download release assets.

This document is a download catalog, not evidence that a dataset
has been downloaded, inspected, or validated.

## Dataset catalog

Detailed checks: `docs/data-validation.md`. Status labels: **Located**, **Downloaded**, **Inspected**, **Validated** (see "Validation status"). Hash values are labelled by origin. Last update: 2026-11-19.

| Dataset | Intended use | Release tag | Exact file | Download link (from API `browser_download_url`) | Size reported by API (bytes) | SHA-256 | Expected local path | Verification status |
|---|---|---|---|---|---|---|---|---|
| IBGE, Census 2022 | Census-sector boundaries and attributes; population variable `v0001` = "Total de pessoas" per the dictionary | `data-v1` | `SP_setores_CD2022.tar.gz` | https://github.com/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases/download/data-v1/SP_setores_CD2022.tar.gz | 90,006,177 | `80134794eed52e47650bb2fd65f19ad294eacd130b22879a2e432b5a7f35173c` (API-provided; independently matched on 2026-11-19 against a locally downloaded copy) | Archive: `data/raw/IBGE/SP_setores_CD2022.tar.gz`; read path: `data/raw/IBGE/SP_setores_CD2022.gpkg` | Downloaded and inspected (see "IBGE inspection record"). Not validated. Dictionary located (`Dicionario_de_dados_malha_agregados.xlsx`) |
| ARTESP, GTFS | Metropolitan bus services near the city border, subject to coverage inspection | `data-artesp-2026-11-09` | `artesp_gtfs.zip` | https://github.com/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases/download/data-artesp-2026-11-09/artesp_gtfs.zip | 46,619,813 | `018af485a0de7a6e13d483b6545ed48cd23b6ce9100adfbadad2fa0e0d5b4e42` (API-provided; not independently verified) | `data/raw/artesp/artesp_gtfs.zip` | Located. Not downloaded or inspected. Redistribution permission pending confirmation with the provider |
| OpenStreetMap / Geofabrik | Street data for pedestrian-access validation | `data-osm-sudeste-2026-11-08` | `sudeste-261108.osm.pbf` | https://github.com/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases/download/data-osm-sudeste-2026-11-08/sudeste-261108.osm.pbf | 863,293,692 | `15bfbd89fa16667e32fda98fa22e90e864cf31c245e9a5d79af880614d52fcdb` (API-provided; not independently verified) | `data/raw/osm/sudeste-261108.osm.pbf` | Located. Not downloaded or inspected. Internal timestamp unverified |
| SPTrans, GTFS | Municipal bus stops, routes, trips, scheduled service | None found in the Releases JSON | `sptrans_gtfs.zip` (in the repository checkout, commit `c8ef414`) | Not applicable (file is in the Git tree) | 14,315,075 (file size, measured) | `4c34deb6e8df4d76b36d11e20acfe3d02139d212b82dd1300d36624cec54aec2` (locally calculated; identical to the copy attached by the owner; no source checksum to compare) | `data/raw/SPTrans/sptrans_gtfs.zip` | Located and inspected (see `docs/data-validation.md`, section GTFS). Feed publication date: Desconhecido nos materiais fornecidos (no `feed_info.txt`) |
| GeoSampa | District and subprefecture boundaries, metro and train stations | None found in the Releases JSON | `distrito_municipal_v2.gpkg` (2,408,448 B), `subprefeitura_v2.gpkg` (1,495,040 B), `estacao_metro_v2.gpkg` (139,264 B), `estacao_trem_v2.gpkg` (143,360 B), all in the checkout | Not applicable (files are in the Git tree) | As listed (measured) | Locally calculated, identical to the owner's attached copies: `cc59fd63fb4f4f106cc8782491b1020f3fe781d82091b2f9f6c6c531cbdd16a2`, `71bde555e877bb4f454baf54710a2d5a764aa9a251ad47e7351149cc235a5191`, `c55327710933a9a20d3bf343c63864e6742a030a3e63c187d31711c9a085db34`, `1a3ff5d150489ccd713f623f4f5e072af7db3f73c4f65ccad2cbf77d131568a8` | `data/raw/geosampa/` | Located and inspected (see `docs/data-validation.md`). Source date and licence: Desconhecido nos materiais fornecidos |

Two different statements are recorded for SPTrans and GeoSampa and must not be confused:
1. The `releases.json` provided on 2026-11-19 lists three releases only; none corresponds to SPTrans or GeoSampa.
2. The files exist in the repository checkout (commit `c8ef414`). Their SHA-256 values equal those of the copies inspected earlier, so that inspection applies to them. This is an identity check, not proof of correctness against the original source.

The three SHA-256 values for ARTESP and OSM are "API-provided; not independently verified" until compared with a downloaded file. The IBGE value was compared on 2026-11-19 and matched.

“Pending verification” means that the relevant information has not
been confirmed for this catalog. It does not mean the dataset is
unavailable.

## Dataset-specific documentation

Consult the corresponding README if it exists in the repository:

| Dataset | Documentation location |
|---|---|
| IBGE | `data/raw/IBGE/README.md` |
| SPTrans | `data/raw/SPTrans/README.md` |
| ARTESP | `data/raw/artesp/README.md` |
| OpenStreetMap | `data/raw/osm/README.md` |
| GeoSampa | `data/raw/geosampa/README.md` |

These paths are relative to the repository root.

When adding clickable links from this document, use paths relative
to `assets/`. For example, a verified IBGE README would be linked as
`../data/raw/IBGE/README.md`.

## Finding release assets

### Using the GitHub website

1. Open the project's Releases page.
2. Select the release corresponding to the required dataset.
3. Expand its Assets section.
4. Locate the dataset by its verified filename.
5. Download the file and place it in the expected local directory.

Do not confuse the automatically generated source-code ZIP or TAR.GZ
archives with dataset assets.

Record the release tag and the exact asset filename used.

### Using the GitHub API

If the Releases page is difficult to access, inspect the public
Releases API:

https://api.github.com/repos/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases

Relevant fields include:

- `tag_name`: release tag.
- `assets[].name`: asset filename.
- `assets[].size`: asset size in bytes.
- `assets[].browser_download_url`: direct download URL.

Example request for an environment with network access:

```bash
curl -fL \
  [https://api.github.com/repos/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases](https://api.github.com/repos/Mindful-AI-Research/4-project-ai-ml-geospatial-transit-desert-mapper/releases)
```

Use the returned download URLs. Do not construct download links
from unverified tags or filenames.

An unsuccessful request does not establish that an asset is missing.
Check the HTTP response, authentication requirements, and environment
network restrictions before drawing conclusions.

Never commit credentials or access tokens to the repository.

## Local organization

```text
data/
├── raw/
│   ├── IBGE/
│   ├── SPTrans/
│   ├── artesp/
│   ├── geosampa/
│   └── osm/
└── processed/
```

Preserve folder capitalization. In particular, `IBGE` and `SPTrans`
must not be silently replaced with lowercase alternatives.

The `assets/` directory contains this catalog. It is not the intended
storage location for the raw datasets.

## Acquisition and extraction

1. Read the dataset-specific documentation.
2. Verify the source or release and the exact filename.
3. Check the download size before transferring large files.
4. Download the original file into its expected raw-data directory.
5. Preserve the original download unchanged.
6. Inspect compressed archives before extraction.
7. Extract working copies into a separate subdirectory when needed.
8. Configure the pipeline to use the actual input path.
9. Save cleaned, filtered, or transformed outputs under
   `data/processed/`.

Do not assume that an archive contains a particular filename or layer.
Avoid maintaining duplicate downloads unless required and documented.

Do not add large raw datasets to Git history.

## Dataset notes

### IBGE — Census 2022

Approved layout: keep the original archive unchanged at
`data/raw/IBGE/SP_setores_CD2022.tar.gz`. Extract only the GeoPackage to
`data/raw/IBGE/SP_setores_CD2022.gpkg` without overwriting an existing file:

```bash
tar -xzk -f data/raw/IBGE/SP_setores_CD2022.tar.gz -C data/raw/IBGE SP_setores_CD2022.gpkg
```

The archive also holds a macOS metadata file (`._SP_setores_CD2022.gpkg`); it is not needed.

Product (from the README link and the file's download metadata): IBGE, Census 2022,
"Agregados por Setores Censitários", "malha com atributos", state of São Paulo.
Exact product version or publication date: Desconhecido nos materiais fornecidos.

Keep statewide source data unchanged and save the São Paulo municipal subset as a derived output.
Do not automatically replace missing population values with zero.

**Variable dictionary.** `data/raw/IBGE/Dicionario_de_dados_malha_agregados.xlsx` is present on branch `main`
(commit `0feb9d4`, byte-identical to the copy provided by the owner, checked by SHA-256 prefix). Sheet `Setor`
defines `V0001` as "Total de pessoas" and `V0002` to `V0007` as household counts and percentages (see
`data/raw/IBGE/README.md`). The dictionary does not document how zeros or suppression are treated.

#### IBGE inspection record (2026-11-19)

Performed on a copy downloaded from the exact API link; the archive was listed before extraction.

| Check | Result |
|---|---|
| Download | HTTP 200; size 90,006,177 bytes, equal to the API value; local SHA-256 equal to the API-provided value |
| Archive contents | Two entries: `SP_setores_CD2022.gpkg` (182,128,640 bytes) and a macOS metadata file `._SP_setores_CD2022.gpkg` (733 bytes). No documentation, dictionary or README inside |
| Provenance hint | The macOS metadata records the source URL as the IBGE FTP folder in the README link. Hint only; not an official statement |
| GeoPackage layers | One feature layer, `SP_setores_CD2022`, polygons, SRS id 4674 (geographic coordinates; reproject to EPSG:31983 before metric work) |
| Field descriptions in the file | None found: no `gpkg_metadata` and no `gpkg_data_columns` tables |
| Rows | 103,620 sectors in the state; 27,301 with `CD_MUN` = `3550308` (`NM_MUN` = São Paulo) |
| Columns (38) | `CD_SETOR`, `SITUACAO`, `CD_SIT`, `CD_TIPO`, `AREA_KM2`, region, state, municipality (`CD_MUN`, `NM_MUN`), district (`CD_DIST`, `NM_DIST`), subdistrict, `NM_BAIRRO`, urban-nucleus and other territorial codes and names, and `v0001` to `v0007` |
| `v0001` to `v0007`, municipality 3550308 | No nulls in any of the seven. `v0001`: min 0, max 2221, sum 11,451,999; 412 sectors have `v0001` = 0. Other columns have different ranges. These are descriptive statistics, not definitions |
| `SITUACAO` | 10 sectors with empty `SITUACAO` (`CD_SIT` = 9), 254 "Rural" and 27,037 "Urbana". The `CD_SIT` and `CD_TIPO` codes are not decoded here |

Not performed in this record: geometry validity and comparison with an external total; see "Additional verifications" below. Variable definitions: see the dictionary correspondence checks below.
Note for the methodology: `v0001` has zeros but no nulls in the municipality, and the dictionary does not document zero or
suppression rules. The sum of `v0001` for the municipality (11,451,999) is not compared with an official total here.

#### IBGE dictionary correspondence checks (2026-11-19, municipality 3550308, 27,301 sectors)

| Check | Result |
|---|---|
| `V0001` definition in sheet `Setor` | "Total de pessoas" |
| GeoPackage field | `v0001` exists (INTEGER), matched by name ignoring case |
| `v0002` = `v0003` + `v0004` (total = private + collective households) | 0 violations |
| `v0007` <= `v0003` (occupied <= private households) | 0 violations |
| `v0001` >= `v0007` (persons >= occupied private households) | 0 violations |
| `CD_SETOR` unique; empty geometry; `AREA_KM2` null or <= 0 | 27,301 unique; 0; 0 |

These checks show that the data are internally consistent with the dictionary. They do not validate the counts
against external IBGE totals. `v0005` was not checked against `v0001 / v0007` because its definition uses persons
in occupied private households, not `v0001`.

Registered population equal to zero ("população registrada igual a zero"): 412 sectors with `v0001` = 0. Mutually exclusive
categories, by household fields (`v0002` total, `v0003` private, `v0004` collective):

| Category | Rule | Sectors |
|---|---|---|
| A | `v0002` = 0 (no households of any kind) | 373 |
| B | `v0002` > 0, `v0003` > 0 and `v0004` > 0 | 1 |
| C | `v0002` > 0, `v0003` > 0, `v0004` = 0 (private households only) | 32 |
| D | `v0002` > 0, `v0003` = 0, `v0004` > 0 (collective households only) | 6 |
| Total | | 412 |

Correction: the earlier statement "33 have `v0001` = 0 but `v0003` > 0" was right (B + C), but it left out the six sectors of
category D, which have only collective households (`v0004` > 0, `v0003` = 0). In all 412 sectors `v0007` = 0.
By `CD_SIT`: 193 (code 1), 155 (code 2), 54 (code 8), 10 (code 9). By `CD_TIPO`: 367 type 4, 25 type 0, 10 type 1, 8 type 7,
1 type 2, 1 type 6. The dictionary lists `CD_SITUACAO` 9 as "Massas de água" and `CD_TIPO` 4 as "Setor com baixo patamar domiciliar".
Whether a zero means no residents, not collected or suppressed is NOT documented: no such meaning is assigned.

#### Additional verifications (2026-11-20)

| Item | Result |
|---|---|
| Dictionary copies | Full SHA-256 compared: attachment and `main` copy (`0feb9d4`) are both `0dffb669ee90e1ffb86a7c8666cc066d5121d44b494013cc1149e50cc75073b1`. Correction: the earlier report compared only a 20-character prefix; the full hashes are now compared and equal |
| Municipal sum of `v0001` | 11,451,999. A secondary source, the municipal health bulletin "Boletim Censo Demográfico 2022 n. 01" (Prefeitura de São Paulo, published November 2024), reports 11.451.999 residents for the municipality in 2022 and cites only "Censo Demográfico 2022, IBGE". Equal values. Limits: this is not an IBGE primary page (the IBGE "cidades e estados" page could not be opened from this environment); neither the IBGE release version nor the census reference date is stated in that source. A comparison with the IBGE primary table, identifying its release and date, is still pending |
| Geometry | Non-empty: 27,301 of 27,301 (0 empty or null). Validity was tested with Shapely `is_valid` on the source geometries: 27,298 valid and 3 invalid, all "Ring Self-intersection" (sectors `355030842000772`, `355030857000168`, `355030858000491`). No repair was applied. All geometries are `Polygon` |

#### Prepared subset (prepared in the review environment, NOT applied to the repository)

Script `src/data/prepare_ibge.py` filters `CD_MUN` = `3550308` (27,301 sectors), keeps all 36 original attribute columns and the geometry,
reprojects from EPSG:4674 to EPSG:31983 and writes `data/processed/ibge_sectors_sao_paulo_epsg31983.gpkg` and
`data/processed/ibge_sectors_sao_paulo_report.json`. It refuses to overwrite existing outputs and never modifies the input. The `id` column of the
source GeoPackage is a feature id and is regenerated by the writer. Input file SHA-256 (extracted GeoPackage):
`07affc966f82292d6f9a359adccc49e69ed55d2075936ef6d1e9c346b29a04bc`. The output was re-read: 27,301 rows, EPSG:31983.

### SPTrans — GTFS

Confirm download completion and inspect the feed before analysis.

Check feed dates, service calendars, stop coordinates, identifiers,
and relationships between stops, routes, trips, and stop times.

Do not treat a scheduled service record as proof of observed operation.

### ARTESP — GTFS

A filename discussed during acquisition was `artesp_gtfs.zip`.
Confirm the actual release asset name before using it.

Inspect geographic coverage, service dates, required tables,
missing records, and overlap with other transport datasets.

Do not assume that all services in the feed are relevant to the
municipality of São Paulo.

### OpenStreetMap / Geofabrik

The filename discussed during acquisition was:

`sudeste-261108.osm.pbf`

Expected local path, if that filename is confirmed:

`data/raw/osm/sudeste-261108.osm.pbf`

The intended extract covers Southeast Brazil. Confirm its actual
coverage and metadata before processing.

Preserve the original PBF file and create study-area extracts as
derived outputs.

Inspect pedestrian access restrictions and network connectivity
before using the network for walking-distance calculations.

Do not describe straight-line distance as street-network distance.

### GeoSampa

The acquisition workflow identified GeoPackage files for:

- Districts.
- Subprefectures.
- Metro stations.
- Train stations.

Confirm exact filenames, layer names, source dates, coordinate
reference systems, and relevant attributes.

Document any overlap between station layers and stops from GTFS
before combining them.

## Provenance record

For each input, record:

| Field | Required information |
|---|---|
| Dataset | Dataset and product name |
| Publisher | Original data provider |
| Source URL | Verified official source |
| Release | Verified project release URL and tag, if applicable |
| Asset | Exact downloaded filename and URL |
| Reference period | Census year, snapshot date, or service period |
| Download date | Actual date of acquisition |
| File size | Downloaded file size |
| Checksum | SHA-256, when calculated |
| License | Dataset-specific terms and attribution |
| Inspection | Layers, tables, schema, and coverage checked |
| Validation | Checks performed, results, and unresolved issues |

Do not infer the download date from the dataset reference date or
the filename.

A checksum calculated locally records the identity of that local
file. It verifies a transfer against the source only when compared
with a trusted source checksum.

## Validation status

Use explicit status descriptions:

- **Located:** a source or download link has been identified.
- **Downloaded:** the file is available in the working environment.
- **Inspected:** its structure and metadata have been examined.
- **Validated:** documented checks have been performed and their
  results recorded.

A dataset may pass some checks while still having unresolved issues.
Record limitations rather than assigning an unconditional
“validated” label.

## Temporal and methodological limitations

Population data refer to Census 2022, while transport feeds and
street-network extracts may refer to later periods.

Record these differences and explain how they affect interpretation.

This catalog does not define:

- Accessibility thresholds.
- Walking speeds.
- Indicator weights.
- Desert-classification rules.
- Ranking criteria.

Document and justify those decisions in the methodology.

Do not present an assumed walking time derived from straight-line
distance as an observed travel time or a routed walking estimate.

## Licensing and attribution

Each dataset remains subject to its own license and terms of use.

The repository's software license does not replace third-party
dataset licenses.

Verify and preserve the attribution requirements for IBGE, SPTrans,
ARTESP, GeoSampa, OpenStreetMap, Geofabrik, and any additional sources
actually used.

Do not assume that redistribution is permitted solely because a file
is publicly downloadable.

## Maintenance

Update this catalog whenever:

- A dataset snapshot changes.
- An asset is added, replaced, or removed.
- A local path changes.
- A direct download link is verified.
- New validation results become available.

Keep the main README, dataset-specific READMEs, pipeline configuration,
and presentation consistent with this document.
