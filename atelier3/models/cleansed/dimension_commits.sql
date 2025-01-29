WITH cleaned_commits AS (
    SELECT
        commit_id,
        author_name,
        author_email,
        commit_date,
        message
    FROM {{ source('raw', 'commits') }}
)

SELECT * FROM cleaned_commits
