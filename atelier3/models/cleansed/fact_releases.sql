WITH aggregated AS (
    SELECT
        id_projet,
        id_release,
        COUNT(*) AS nombre_releases
    FROM {{ source('raw', 'fact_releases') }}
    GROUP BY id_projet, id_release
)
SELECT * FROM aggregated;
