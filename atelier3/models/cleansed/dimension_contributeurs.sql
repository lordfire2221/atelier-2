WITH cleaned_contributors AS (
    SELECT
        contributor_id,
        contributor_name,
        contributor_email,
        registration_date
    FROM {{ source('raw', 'contributors') }}
)

SELECT * FROM cleaned_contributors
