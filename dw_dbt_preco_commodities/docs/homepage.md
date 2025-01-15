{% docs __overview__ %}

### README do projeto DBT-core

# Projeto DBT-core para Data Warehouse de Commodities

Este projeto utiliza DBT

''' mermaid

flowchart TD
A[Extrair Dados de Commodities] --> B[Transformar Dados]
B --> C[Carregar no PostgreSQL]

    subgraph Extrair
        A1[buscar_dados_commodities]
        A2[buscar_todos_dados_commodities]
        A1 --> A2
    end

    subgraph Transformar
        T1[Filtrar coluna 'Close']
        T2[Adicionar coluna 'simbolo']
        A2 --> T1 --> T2
    end

    subgraph Carregar
        C1[salvar_no_postgres]
        T2 --> C1
    end

'''

## Estrutura do Projeto

### 1. Seeds

Os seed's são os dados estaticos que são carregados pra o Data Warehouse a partir de arquivos csb (,)

### 2. Models

#### 3. Staging

A Camada Staging é responsavel por...

-   **stg_commodities.sql** : ttt

-   **stg_commodities.sql** : ttt

#### Datamart

{% enddocs %}
