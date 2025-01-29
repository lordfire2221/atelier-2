WITH cleaned_projects AS (
    SELECT
        project_id,
        project_name,
        description,
        start_date,
        end_date,
        status
    FROM {{ source('raw', 'projects') }}
)

SELECT * FROM cleaned_projects
