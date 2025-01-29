WITH cleaned_project_activity AS (
    SELECT
        project_id,
        activity_type,
        activity_date,
        activity_duration
    FROM {{ source('raw', 'fact_activite_projet') }}
)

SELECT * FROM cleaned_project_activity
