# Data Validation Record

Scope: checks actually performed on the input data of the São Paulo Transit Desert Mapper, between 2026-11-19 and 2026-11-20,
in a cloud review environment (not the owner's machine). Repository checkout: `c8ef414`; branch `main` fetched at `0feb9d4`.
This record states what was verified, how, and what is still pending. A dataset that passes some checks is not thereby "validated"
without qualification.

Analytical notice: "Índice analítico baseado em dados abertos e em limiares escolhidos pelo grupo. Não mede a qualidade do serviço nem substitui diagnóstico de campo."

## Summary

| Area | Status |
|---|---|
| IBGE file integrity and identity | Completed |
| IBGE dictionary and `v0001` definition | Completed |
| IBGE internal consistency of household fields | Completed |
| Municipal population total against an external source | Partly completed; primary IBGE comparison pending |
| Zero values and suppression rules | Descriptive only; rules not documented, none assumed |
| Geometry validity | Completed; 3 invalid geometries, treatment pending |
| Hashes of project inputs | Completed for the files available; ARTESP and OSM not downloaded |
| GTFS (SPTrans) audit | Completed for structure; service-date and coverage questions pending |
| GeoSampa layers | Inspected earlier; source date and licence pending |
| Validation of results (accessibility indicators) | Not started |

## 1. IBGE, Census 2022 sectors

### 1.1 Download and hashes

| Item | Value |
|---|---|
| Method | Downloaded from the exact `browser_download_url` in `releases.json`; size and SHA-256 computed locally |
| Result | HTTP 200; 90,006,177 bytes, equal to the API size; SHA-256 `80134794eed52e47650bb2fd65f19ad294eacd130b22879a2e432b5a7f35173c`, equal to the API-provided digest |
| Extracted GeoPackage SHA-256 | `07affc966f82292d6f9a359adccc49e69ed55d2075936ef6d1e9c346b29a04bc` (local identity only) |
| Source | `releases.json` (owner), release `data-v1` |
| Limitation | A match with the API digest verifies the transfer from the release, not the content against IBGE's original |

Archive listing before extraction: `SP_setores_CD2022.gpkg` (182,128,640 bytes) and `._SP_setores_CD2022.gpkg` (733 bytes, macOS metadata, not needed). No documentation inside.

### 1.2 Dictionary

| Item | Value |
|---|---|
| Method | Opened `Dicionario_de_dados_malha_agregados.xlsx` (sheets `Setor`, `Distrito`, `Subdistrito`, `Bairro`); read sheet `Setor`; compared the copy attached by the owner with the copy on `main` (`0feb9d4`) by full SHA-256 |
| Result | Both copies: `0dffb669ee90e1ffb86a7c8666cc066d5121d44b494013cc1149e50cc75073b1`. `V0001` = "Total de pessoas"; `V0002` total households; `V0003` private households; `V0004` collective households; `V0005` average residents in occupied private households; `V0006` percentage of imputed occupied private households; `V0007` occupied private households |
| Correspondence | GeoPackage fields `v0001` to `v0007` exist (lowercase) and match the dictionary names ignoring case. Name differences: `CD_SUBDIS` (dictionary) vs `CD_SUBDIST`; `CD_SITUACAO` vs `CD_SIT` |
| Source | Dictionary file in the repository |
| Limitations | The dictionary does not state the census reference date, the file version, or any rule for zero values or suppression. Correction note: an earlier report compared only a 20-character prefix of the hashes; the full hashes are compared here |

### 1.3 Internal consistency (municipality 3550308, 27,301 sectors)

| Check | Result |
|---|---|
| `v0002` = `v0003` + `v0004` | 0 violations |
| `v0007` <= `v0003` | 0 violations |
| `v0001` >= `v0007` | 0 violations |
| `CD_SETOR` unique | 27,301 unique |
| Empty or null geometry; `AREA_KM2` null or <= 0 | 0; 0 |
| `v0001` null | 0 |
| Method | SQL queries on the GeoPackage opened read-only (Python `sqlite3`) |
| Limitation | Consistency with the dictionary definitions, not accuracy against the census. `v0005` was not recomputed because its numerator is persons in occupied private households, not `v0001` |

### 1.4 Population total

| Item | Value |
|---|---|
| Method | Sum of `v0001` over municipality 3550308 |
| Result | 11,451,999 |
| External comparison | Boletim Censo Demográfico 2022 n. 01, Prefeitura de São Paulo, published November 2024, reports 11.451.999 residents for 2022. Values are equal |
| Limitations | Secondary source that cites only "Censo Demográfico 2022, IBGE". It states neither the IBGE release version nor the census reference date. The IBGE "cidades e estados" page could not be opened from the review environment |
| Pending | Compare with the IBGE primary table, identifying its release and reference date |

### 1.5 Zero values ("população registrada igual a zero")

| Category | Rule | Sectors |
|---|---|---|
| A | `v0002` = 0 | 373 |
| B | `v0002` > 0, `v0003` > 0, `v0004` > 0 | 1 |
| C | `v0002` > 0, `v0003` > 0, `v0004` = 0 | 32 |
| D | `v0002` > 0, `v0003` = 0, `v0004` > 0 | 6 |
| Total | `v0001` = 0 | 412 |

In all 412 sectors `v0007` = 0. By `CD_SIT`: 193 (1), 155 (2), 54 (8), 10 (9). By `CD_TIPO`: 367 (4), 25 (0), 10 (1), 8 (7), 1 (2), 1 (6).
The dictionary lists `CD_SITUACAO` 9 as "Massas de água" and `CD_TIPO` 4 as "Setor com baixo patamar domiciliar".
Limitation and decision: the sources do not say whether a zero means no residents, not collected, or suppressed. No such meaning is assigned.
Values are preserved without imputation. These sectors stay in territorial coverage and audit and are outside the population-affected ranking.

### 1.6 Geometry

| Item | Value |
|---|---|
| Method | Shapely 2.2.0 `is_valid` on the source geometries of the 27,301 sectors; `explain_validity` for reasons |
| Result | All `Polygon`. 0 empty or null. 27,298 valid; 3 invalid, all "Ring Self-intersection": `355030842000772`, `355030857000168`, `355030858000491` |
| Repair | None applied (`geometry_repaired` = false in the report) |
| Pending | Decide treatment (for example `make_valid` as a documented derived step, or exclusion with a count). No repair attempt has been executed. No authorization of a repair attempt appears in the messages received by the review environment; a repair attempt, once authorized, still needs review and explicit acceptance of its result |

### 1.7 Prepared subset

`src/data/prepare_ibge.py` filters `CD_MUN` = `3550308`, keeps all original attribute columns, reprojects EPSG:4674 to EPSG:31983, writes
`data/processed/ibge_sectors_sao_paulo_epsg31983.gpkg` and `data/processed/ibge_sectors_sao_paulo_report.json`, and refuses to overwrite.
Re-reading the output: 27,301 rows, EPSG:31983. Prepared in the review environment; applied to the repository only when the owner adds the files.

## 2. SPTrans GTFS audit

| Check | Result |
|---|---|
| Method | Read `data/raw/SPTrans/sptrans_gtfs.zip` with Python `zipfile` and `csv`; no feed modification |
| File | 14,315,075 bytes; SHA-256 `4c34deb6e8df4d76b36d11e20acfe3d02139d212b82dd1300d36624cec54aec2`, identical to the copy attached by the owner (local identity; no source checksum) |
| Tables | `agency`, `calendar`, `fare_attributes`, `fare_rules`, `frequencies`, `routes`, `shapes`, `stop_times`, `stops`, `trips`. No `feed_info.txt` |
| Stops | 22,273; `stop_id` unique; no missing coordinates; latitude -23.911109 to -23.195643, longitude -46.983953 to -46.18493; columns `stop_id`, `stop_name`, `stop_desc`, `stop_lat`, `stop_lon` (no `location_type`) |
| Routes | 1,365: 1,349 bus (type 3), 9 metro (1), 7 rail (2) |
| Trips | 2,268. All have `stop_times`; all appear in `frequencies`; no `stop_times` row refers to a missing trip |
| `stop_times` | 99,120 rows; all 22,273 stops appear in it |
| `frequencies` | 40,337 rows, columns `trip_id`, `start_time`, `end_time`, `headway_secs` (no `exact_times`) |
| `calendar` | 6 service patterns, 2023-10-01 to 2027-06-01 |
| Interpretation | The small `stop_times` is consistent with a frequency-based feed: one reference sequence per trip, with service expressed in `frequencies`. This replaces the earlier worry that it was a reduced extract; it does not prove the feed is complete |
| Limitations | Feed publication date, version and completeness against SPTrans' full network: Desconhecido nos materiais fornecidos. GTFS is scheduled supply, not observed operation. Metro and rail stops by route type (109 and 104) differ from the GeoSampa station layers (94 and 109): not merged by proximity; reconcile before use |
| Pending | Define the service window for "served" (day type, time band, minimum departures) from `calendar` and `frequencies`; check overlap with ARTESP |

## 3. GeoSampa layers

| Item | Value |
|---|---|
| Method | Opened the four GeoPackages; compared SHA-256 of the checkout copies with the owner's attached copies |
| Result | Hashes equal (listed in `assets/dataset-sources-and-downloads.md`). All EPSG:31983. `distrito_municipal_v2`: 96 polygons; `subprefeitura_v2`: 32 polygons; `estacao_metro_v2`: 94 points, all "OPERANDO"; `estacao_trem_v2`: 109 points, all "OPERANDO" |
| Limitations | Source date, licence and attribution: Desconhecido nos materiais fornecidos. Geometry validity not tested |

## 4. Files located but not downloaded

| Asset | Reported by API | Status |
|---|---|---|
| `artesp_gtfs.zip` (46,619,813 B) | sha256 `018af485a0de7a6e13d483b6545ed48cd23b6ce9100adfbadad2fa0e0d5b4e42` | API-provided; not independently verified. Redistribution permission pending confirmation with ARTESP |
| `sudeste-261108.osm.pbf` (863,293,692 B) | sha256 `15bfbd89fa16667e32fda98fa22e90e864cf31c245e9a5d79af880614d52fcdb` | API-provided; not independently verified. Internal timestamp unverified. Licence ODbL, attribution "OpenStreetMap contributors" |

## 5. Pending items

1. IBGE primary total and release identification.
2. Treatment of the 3 invalid geometries.
3. Rules for zero and suppression: only if IBGE documents them; none assumed.
4. GTFS service window, feed date and completeness; overlap with ARTESP.
5. GeoSampa source date and licence; station reconciliation with GTFS.
6. Download and inspection of ARTESP and OSM when needed.
7. Validation of the indicators themselves (not started).
