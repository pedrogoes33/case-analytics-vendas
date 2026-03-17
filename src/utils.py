from __future__ import annotations

from pathlib import Path
import pandas as pd


CATEGORY_MAP = {
    "MS": "metal",
    "LS": "louças",
    "RC": "cerâmica",
}


def carregar_dados(csv_path: str | Path) -> pd.DataFrame:
    """
    Lê o arquivo CSV e aplica os tratamentos mínimos para a análise.

    Regras adotadas:
    - converte datas
    - converte colunas numéricas
    - cria a coluna 'categoria'
    """
    df = pd.read_csv(csv_path)

    df["mes_ref"] = pd.to_datetime(df["mes_ref"], errors="coerce")
    df["data_competencia"] = pd.to_datetime(df["data_competencia"], errors="coerce")

    numeric_cols = [
        "Receita_faturada",
        "Volume_faturado",
        "Receita_vendida",
        "Volume_vendido",
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["categoria"] = df["codigo_setor_atividade"].map(CATEGORY_MAP).fillna(
        df["codigo_setor_atividade"].astype(str)
    )

    return df


def filtrar_base_analitica(df: pd.DataFrame) -> pd.DataFrame:
    """
    Mantém somente registros com venda efetiva (> 0 em receita ou volume vendido).

    Motivo:
    o dataset possui linhas de cancelamento, devolução e faturamento com valores zerados
    ou negativos. Para responder ao case com foco em performance de vendas, usamos
    somente pedidos com venda positiva.
    """
    return df[(df["Receita_vendida"] > 0) | (df["Volume_vendido"] > 0)].copy()


def formatar_moeda(valor: float) -> str:
    valor_formatado = f"R$ {valor:,.2f}"
    return valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")


def garantir_pasta(path: str | Path) -> Path:
    destino = Path(path)
    destino.mkdir(parents=True, exist_ok=True)
    return destino