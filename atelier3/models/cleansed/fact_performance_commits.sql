WITH cleaned_commit_performance AS (
    SELECT
        commit_id,
        lines_added,
        lines_deleted,
        files_changed
    FROM {{ source('raw', 'fact_performance_commits') }}
)

SELECT * FROM cleaned_commit_performance
