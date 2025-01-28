WITH filtered AS (
    SELECT
        id_projet,
        nom,
        description,
        nombre_stars,
        nombre_forks
    FROM {{ source('raw', 'dimension_projets') }}
    WHERE nombre_stars > 0
)
SELECT * FROM filtered;
