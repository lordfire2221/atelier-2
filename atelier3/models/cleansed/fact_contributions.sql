WITH cleaned_contributions AS (
    SELECT
        contributor_id,
        project_id,
        commit_id,
        contribution_date
    FROM {{ source('raw', 'fact_contributions') }}
)

SELECT * FROM cleaned_contributions
