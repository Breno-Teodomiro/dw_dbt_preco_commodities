-- Import
with 
source as (
     select
            "Data"
          , "Close"
          , "simbolo"
       from {{ source ('bd_btc', 'commodities') }}
),

-- Renamed
Renamed as (
     select
            cast("Data" as date) as data
          , "Close" as preco_fechamento
          , "simbolo" as ticker
       from source
)

-- Select
     select
            *
       from Renamed
