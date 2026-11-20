
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

Local paths below follow the project structure discussed during
data acquisition. Confirm that they match the current repository
before running the pipeline.

| Dataset | Intended use | Expected local directory | Download location | Direct asset link | Validation status |
|---|---|---|---|---|---|
| IBGE — Census 2022 | Census-sector boundaries and population data, subject to schema verification | `data/raw/IBGE/` | Project Releases or official IBGE source | Pending verification | Archive contents, layers, and population variable pending verification |
| SPTrans — GTFS | Municipal bus stops, routes, trips, and scheduled service | `data/raw/SPTrans/` | Official SPTrans source; check Releases for a project snapshot | Pending verification | Download completion and feed contents pending verification |
| ARTESP — GTFS | Additional transport services relevant to the study area, subject to coverage inspection | `data/raw/artesp/` | Project Releases or official ARTESP source | Pending verification | Asset availability, service coverage, and validity dates pending verification |
| OpenStreetMap / Geofabrik | Street-network data for pedestrian-access analysis | `data/raw/osm/` | Project Releases or official Geofabrik source | Pending verification | Download completion, file integrity, and network suitability pending verification |
| GeoSampa | Administrative boundaries and rail-station layers selected for the project | `data/raw/geosampa/` | Official GeoSampa source; check Releases for project snapshots | Pending verification | Exact filenames, layer metadata, and geometry checks pending verification |

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

Inspect the downloaded archive or GeoPackage before selecting inputs.

Verify:

- Available layers and geographic coverage.
- Census-sector identifiers.
- Municipality field and the code for São Paulo municipality.
- Population variable and its documented definition.
- Missing, suppressed, or special values.
- Coordinate reference system and geometry validity.
- Compatibility of identifiers used for joins.

Do not assume that `v0001`, or any other field, represents population
without consulting the dictionary for the exact dataset and table.

Do not automatically replace missing population values with zero.

Keep statewide source data unchanged and save the São Paulo municipal
subset as a derived output.

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
