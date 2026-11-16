SELECT count(id) AS output FROM {{ source('raw','sales') }}
