WITH cleaned_release_facts AS (
    SELECT
        release_id,
        project_id,
        total_downloads,
        total_contributors
    FROM {{ source('raw', 'fact_releases') }}
)

SELECT * FROM cleaned_release_facts
