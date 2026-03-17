# Case - Análise de Vendas com Python

Este repositório resolve o desafio técnico de análise de dados descrito no case enviado pela empresa.

## Objetivo do projeto

Responder às perguntas de negócio:

- quais são os produtos mais vendidos
- qual é o faturamento por mês
- qual é o ticket médio por cliente

Além disso, na branch `develop`, foi adicionada a análise de **top 10 produtos por categoria** (`metal`, `louças` e `cerâmica`), conforme solicitado no case.

## Principais decisões do código

### 1. Base analítica usada
O dataset possui registros com valores:

- zerados
- negativos
- associados a cancelamento/devolução

Para focar no desempenho real de vendas, a análise principal foi construída com os registros em que:

- `Receita_vendida > 0` **ou**
- `Volume_vendido > 0`

Assim, o projeto mede **venda efetiva**, não eventos administrativos ou reversões.

### 2. Métrica de produto mais vendido
O ranking foi calculado com a soma de `Volume_vendido` por produto.

### 3. Métrica de faturamento mensal
O faturamento mensal foi calculado com a soma de `Receita_vendida`, agrupada por `mes_ref`.

### 4. Métrica de ticket médio
O ticket médio foi calculado em duas etapas:

1. somar a `Receita_vendida` por cliente (`cpf_cnpj`)
2. calcular a média dessa receita consolidada entre os clientes

## Estrutura do projeto

```text
case_analytics_vendas/
├── data/
│   └── CASE Vaga SR.csv
├── outputs/
│   ├── charts/
│   │   ├── faturamento_mensal.png
│   │   └── top10_produtos.png
│   └── reports/
│       ├── faturamento_mensal.csv
│       ├── ranking_produtos.csv
│       ├── receita_por_cliente.csv
│       ├── top10_clientes.csv
│       ├── top10_produtos_por_categoria.csv
│       └── top10_produtos_por_receita.csv
├── src/
│   ├── analysis.py
│   └── utils.py
├── .gitignore
├── GUIA_GITHUB_PASSO_A_PASSO.md
├── README.md
└── requirements.txt
```

## Bibliotecas necessárias

Crie e ative um ambiente virtual, depois instale as dependências:

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como executar o script

Na raiz do projeto, rode:

```bash
python src/analysis.py
```

Se quiser informar caminhos manualmente:

```bash
python src/analysis.py --input "data/CASE Vaga SR.csv" --output "outputs"
```

## Saídas geradas

Depois da execução, o projeto gera:

- relatórios em CSV dentro de `outputs/reports`
- gráficos em PNG dentro de `outputs/charts`

## Resultado encontrado nesta base

### Ticket médio por cliente
**R$ 183.782,28**

### Top 5 produtos por volume vendido
|   posicao | codigo_produto   | produto                               |   Volume_vendido |
|----------:|:-----------------|:--------------------------------------|-----------------:|
|         1 | 4509.202         | BASE REG DE GAVETA 3/4 DN20-B         |      3.23735e+06 |
|         2 | 4416.202         | BASE REG PRESSAO MVS 3/4 DN20-B       |      2.11299e+06 |
|         3 | 4686.325         | SCJ REPARO VALV HYDRA MAX 11/4 E 11/2 | 982936           |
|         4 | 4900.C35.PQ      | ACAB P/REG 1/2,3/4E1 PQ ASPEN-CR      | 898243           |
|         5 | 6059800A         | YORK SGR                              | 736685           |

### Faturamento mensal
| ano_mes   |   Receita_vendida |
|:----------|------------------:|
| 2025-01   |       2.11647e+08 |
| 2025-02   |       2.60357e+08 |
| 2025-03   |       2.55283e+08 |
| 2025-04   |       2.45996e+08 |
| 2025-05   |       2.65941e+08 |
| 2025-06   |       3.1067e+08  |
| 2025-07   |       2.4504e+08  |
| 2025-08   |       2.61862e+08 |
| 2025-09   |       2.8982e+08  |
| 2025-10   |       2.76337e+08 |
| 2025-11   |       2.33943e+08 |
| 2025-12   |       2.57436e+08 |
| 2026-01   |       2.08824e+08 |
| 2026-02   |       2.8982e+08  |

## Análises extras adicionadas
Além do que o case pede, o projeto também entrega:

- top 10 clientes por receita
- top 10 produtos por receita
- gráficos de apoio
- top 10 produtos por categoria

## Evolução na branch develop

Na branch `develop`, foi adicionada uma análise complementar para trazer o top 10 produtos por categoria, conforme solicitado no case.


## Sugestão de fluxo no GitHub

1. subir o projeto na branch `main`
2. criar a branch `develop`
3. adicionar a análise de top 10 por categoria
4. abrir um Pull Request de `develop` para `main`

