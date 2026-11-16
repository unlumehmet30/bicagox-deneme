-- Report the synthetic record count.
SELECT count(id) AS output FROM {{ source('raw','sales') }}
