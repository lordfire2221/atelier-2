WITH filtered AS (
    SELECT
        id_contributeur,
        nom,
        localisation,
        nombre_contributions
    FROM {{ source('raw', 'dimension_contributeurs') }}
    WHERE nombre_contributions > 0
)
SELECT * FROM filtered;
