WITH filtered AS (
    SELECT
        id_contribution,
        id_contributeur,
        id_projet,
        DATE(date_contribution) AS date_contribution
    FROM {{ source('raw', 'fact_contributions') }}
)
SELECT * FROM filtered;
