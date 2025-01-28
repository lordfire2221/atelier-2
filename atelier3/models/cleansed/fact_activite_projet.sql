WITH aggregated AS (
    SELECT
        id_projet,
        id_temps,
        SUM(nombre_commits) AS total_commits,
        SUM(nombre_issues_ouvertes) AS total_issues_ouvertes,
        SUM(nombre_issues_closes) AS total_issues_closes,
        SUM(nombre_releases) AS total_releases
    FROM {{ source('raw', 'fact_activite_projet') }}
    GROUP BY id_projet, id_temps
)
SELECT * FROM aggregated;
