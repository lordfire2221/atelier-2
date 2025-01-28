WITH normalized AS (
    SELECT
        id_commit,
        auteur,
        message,
        DATE(date_commit) AS date_commit
    FROM {{ source('raw', 'dimension_commits') }}
)
SELECT * FROM normalized;
