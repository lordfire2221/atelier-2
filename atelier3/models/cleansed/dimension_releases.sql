WITH cleaned AS (
    SELECT
        id_release,
        nom,
        version,
        date_publication,
        TRIM(description) AS description_clean,
        EXTRACT(YEAR FROM date_publication) AS annee_publication
    FROM {{ source('raw', 'dimension_releases') }}
    WHERE date_publication IS NOT NULL
)
SELECT * FROM cleaned;
