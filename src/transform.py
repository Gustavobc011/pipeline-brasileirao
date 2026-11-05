"""Etapa 2 do ETL: Transformar (limpar e enriquecer com pandas)."""
import pandas as pd

# Nomes diferentes para o mesmo clube (confirme com o comando acima)
PADRONIZAR_TIMES = {"Gremio Prudente": "Barueri"}

COLUNAS_UTEIS = [
    "ID", "rodada", "data", "ano", "mandante", "visitante",
    "mandante_Placar", "visitante_Placar", "gols_total", "resultado", "arena",
]


def transformar(df: pd.DataFrame) -> pd.DataFrame:
    """Recebe o DataFrame bruto e devolve o DataFrame tratado."""
    df = df.copy()  # trabalha numa cópia, sem alterar o original

    df = df.rename(columns={"rodata": "rodada"})  # corrige o nome da coluna

    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
    df["ano"] = df["data"].dt.year

    df["mandante"] = df["mandante"].replace(PADRONIZAR_TIMES)
    df["visitante"] = df["visitante"].replace(PADRONIZAR_TIMES)

    df["gols_total"] = df["mandante_Placar"] + df["visitante_Placar"]
    df["resultado"] = "Empate"
    df.loc[df["mandante_Placar"] > df["visitante_Placar"], "resultado"] = "Casa"
    df.loc[df["mandante_Placar"] < df["visitante_Placar"], "resultado"] = "Visitante"

    df = df.drop_duplicates(subset="ID")  # remove jogos repetidos, se houver

    return df[COLUNAS_UTEIS]  # fica só com as colunas que vamos usar