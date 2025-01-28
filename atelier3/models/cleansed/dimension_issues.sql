WITH filtered AS (
    SELECT
        id_issue,
        titre,
        etat,
        DATE(date_creation) AS date_creation,
        DATE(date_cloture) AS date_cloture
    FROM {{ source('raw', 'dimension_issues') }}
    WHERE etat IN ('open', 'closed')
)
SELECT * FROM filtered;
