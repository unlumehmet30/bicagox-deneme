SELECT email AS output FROM {{ source('raw','sales') }}
