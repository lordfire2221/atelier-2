WITH cleaned_time AS (
    SELECT
        id_temps,
        jour,
        mois,
        trimestre,
        annee,
        DATE(annee || '-' || mois || '-' || jour) AS date_complete,
        CASE
            WHEN trimestre = 1 THEN 'Hiver'
            WHEN trimestre = 2 THEN 'Printemps'
            WHEN trimestre = 3 THEN 'Été'
            WHEN trimestre = 4 THEN 'Automne'
        END AS saison
    FROM {{ source('raw', 'dimension_temps') }}
)

SELECT * FROM cleaned_time
