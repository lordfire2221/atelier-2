WITH metrics AS (
    SELECT
        id_commit,
        id_projet,
        id_contributeur,
        performance_score
    FROM {{ source('raw', 'fact_performance_commits') }}
    WHERE performance_score IS NOT NULL
)
SELECT * FROM metrics;
