WITH cleaned_releases AS (
    SELECT
        release_id,
        project_id,
        version,
        release_date,
        description
    FROM {{ source('raw', 'releases') }}
)

SELECT * FROM cleaned_releases
