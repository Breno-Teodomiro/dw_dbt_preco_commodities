-- Import
with source as (
     select
            date
          , symbol
          , action
          , quantity
       from {{ source ('bd_btc', 'movimentacao_commodities') }}
),

-- Renamed
Renamed as (
     select
            cast(date as date) as data
          , symbol as simbolo
          , action as acao
          , quantity as quantidade
       from source
)

-- Select
     select
            *
       from Renamed
