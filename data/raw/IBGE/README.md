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
in the official directory.

## Expected local structure

If downloading a compressed archive, preserve its original filename
and extract its contents into a separate subfolder:

    data/raw/IBGE/
    ├── <original-archive-filename>.tar.gz
    └── extracted/
        └── SP_setores_CD2022.gpkg

The archive filename above is a placeholder. Check the actual filename
and archive contents rather than assuming them.

If downloading the GeoPackage directly, use:

    data/raw/IBGE/SP_setores_CD2022.gpkg

Configure the pipeline to use the actual GeoPackage path.
Do not assume that both download layouts exist.

Release assets are stored separately from the Git source tree.
Cloning the repository does not download this dataset automatically.

## Validation before analysis

Before using the dataset:

1. Confirm that the download is complete and the file opens successfully.
2. Inspect available layers and their documentation.
3. Identify the census-sector identifier and municipality field.
4. Verify the population variable and its definition.
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
