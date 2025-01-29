WITH cleaned_issues AS (
    SELECT
        issue_id,
        project_id,
        title,
        description,
        created_at,
        closed_at,
        status
    FROM {{ source('raw', 'issues') }}
)

SELECT * FROM cleaned_issues
