from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from utils import carregar_dados, filtrar_base_analitica, formatar_moeda, garantir_pasta


def ranking_produtos(df: pd.DataFrame) -> pd.DataFrame:
    ranking = (
        df.groupby(["codigo_produto", "produto"], as_index=False)["Volume_vendido"]
        .sum()
        .sort_values("Volume_vendido", ascending=False)
        .reset_index(drop=True)
    )
    ranking.insert(0, "posicao", ranking.index + 1)
    return ranking


def faturamento_mensal(df: pd.DataFrame) -> pd.DataFrame:
    faturamento = (
        df.assign(ano_mes=df["mes_ref"].dt.to_period("M").astype(str))
        .groupby("ano_mes", as_index=False)["Receita_vendida"]
        .sum()
        .sort_values("ano_mes")
        .reset_index(drop=True)
    )
    return faturamento


def ticket_medio_por_cliente(df: pd.DataFrame) -> tuple[float, pd.DataFrame]:
    receita_por_cliente = (
        df.groupby("cpf_cnpj", as_index=False)["Receita_vendida"]
        .sum()
        .sort_values("Receita_vendida", ascending=False)
        .reset_index(drop=True)
    )
    ticket_medio = receita_por_cliente["Receita_vendida"].mean()
    return ticket_medio, receita_por_cliente


def top10_por_categoria(df: pd.DataFrame) -> pd.DataFrame:
    top10 = (
        df.groupby(["categoria", "codigo_produto", "produto"], as_index=False)["Volume_vendido"]
        .sum()
        .sort_values(["categoria", "Volume_vendido"], ascending=[True, False])
        .reset_index(drop=True)
    )
    top10["rank_categoria"] = (
        top10.groupby("categoria")["Volume_vendido"]
        .rank(method="first", ascending=False)
        .astype(int)
    )
    top10 = top10[top10["rank_categoria"] <= 10].copy()
    return top10.sort_values(["categoria", "rank_categoria"]).reset_index(drop=True)


def top10_clientes(df: pd.DataFrame) -> pd.DataFrame:
    top_clientes = (
        df.groupby("cpf_cnpj", as_index=False)["Receita_vendida"]
        .sum()
        .sort_values("Receita_vendida", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )
    top_clientes.insert(0, "posicao", top_clientes.index + 1)
    return top_clientes


def top10_produtos_por_receita(df: pd.DataFrame) -> pd.DataFrame:
    top_receita = (
        df.groupby(["codigo_produto", "produto"], as_index=False)["Receita_vendida"]
        .sum()
        .sort_values("Receita_vendida", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )
    top_receita.insert(0, "posicao", top_receita.index + 1)
    return top_receita


def salvar_relatorios(
    ranking: pd.DataFrame,
    faturamento: pd.DataFrame,
    receita_por_cliente: pd.DataFrame,
    top10_categoria_df: pd.DataFrame,
    top_clientes_df: pd.DataFrame,
    top_receita_df: pd.DataFrame,
    output_dir: Path,
) -> None:
    reports_dir = garantir_pasta(output_dir / "reports")

    ranking.to_csv(reports_dir / "ranking_produtos.csv", index=False)
    faturamento.to_csv(reports_dir / "faturamento_mensal.csv", index=False)
    receita_por_cliente.to_csv(reports_dir / "receita_por_cliente.csv", index=False)
    top10_categoria_df.to_csv(reports_dir / "top10_produtos_por_categoria.csv", index=False)
    top_clientes_df.to_csv(reports_dir / "top10_clientes.csv", index=False)
    top_receita_df.to_csv(reports_dir / "top10_produtos_por_receita.csv", index=False)


def salvar_graficos(
    ranking: pd.DataFrame,
    faturamento: pd.DataFrame,
    output_dir: Path,
) -> None:
    charts_dir = garantir_pasta(output_dir / "charts")

    plt.figure(figsize=(12, 6))
    plt.bar(faturamento["ano_mes"], faturamento["Receita_vendida"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Faturamento mensal")
    plt.xlabel("Mês")
    plt.ylabel("Receita vendida")
    plt.tight_layout()
    plt.savefig(charts_dir / "faturamento_mensal.png", dpi=150)
    plt.close()

    top10 = ranking.head(10).sort_values("Volume_vendido")
    plt.figure(figsize=(12, 6))
    plt.barh(top10["produto"], top10["Volume_vendido"])
    plt.title("Top 10 produtos por volume vendido")
    plt.xlabel("Volume vendido")
    plt.ylabel("Produto")
    plt.tight_layout()
    plt.savefig(charts_dir / "top10_produtos.png", dpi=150)
    plt.close()


def imprimir_resumo(
    ranking: pd.DataFrame,
    faturamento: pd.DataFrame,
    ticket_medio: float,
) -> None:
    print("\n=== RESUMO DA ANÁLISE ===")
    print("\nTop 10 produtos por volume vendido:")
    print(ranking.head(10).to_string(index=False))

    print("\nFaturamento por mês:")
    print(faturamento.to_string(index=False))

    print(f"\nTicket médio por cliente: {formatar_moeda(ticket_medio)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Análise descritiva do case de vendas.")
    parser.add_argument(
        "--input",
        default="data/CASE Vaga SR.csv",
        help="Caminho do arquivo CSV de entrada.",
    )
    parser.add_argument(
        "--output",
        default="outputs",
        help="Pasta onde os relatórios e gráficos serão salvos.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    csv_path = Path(args.input)
    output_dir = Path(args.output)

    df = carregar_dados(csv_path)
    base = filtrar_base_analitica(df)

    ranking = ranking_produtos(base)
    faturamento = faturamento_mensal(base)
    ticket_medio, receita_por_cliente = ticket_medio_por_cliente(base)
    top10_categoria_df = top10_por_categoria(base)
    top_clientes_df = top10_clientes(base)
    top_receita_df = top10_produtos_por_receita(base)

    salvar_relatorios(
        ranking=ranking,
        faturamento=faturamento,
        receita_por_cliente=receita_por_cliente,
        top10_categoria_df=top10_categoria_df,
        top_clientes_df=top_clientes_df,
        top_receita_df=top_receita_df,
        output_dir=output_dir,
    )
    salvar_graficos(ranking=ranking, faturamento=faturamento, output_dir=output_dir)
    imprimir_resumo(ranking=ranking, faturamento=faturamento, ticket_medio=ticket_medio)


if __name__ == "__main__":
    main()