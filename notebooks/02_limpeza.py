"""Primeira limpeza e primeiras perguntas."""
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

df = pd.read_csv("data/raw/brasileirao.csv")

# 1. Data: de texto ("29/03/2003") para data de verdade
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
df["ano"] = df["data"].dt.year

# 2. O "-" no vencedor significa empate: deixamos isso explícito
df["vencedor"] = df["vencedor"].replace("-", "Empate")

# 3. Colunas novas
df["gols_total"] = df["mandante_Placar"] + df["visitante_Placar"]
df["resultado"] = "Empate"
df.loc[df["mandante_Placar"] > df["visitante_Placar"], "resultado"] = "Casa"
df.loc[df["mandante_Placar"] < df["visitante_Placar"], "resultado"] = "Visitante"

# 4. Conferir se deu certo
print(df[["data", "ano", "mandante", "visitante", "gols_total", "resultado"]].head())

times = sorted(pd.concat([df["mandante"], df["visitante"]]).unique())
print("\nQuantidade de nomes de times:", len(times))
print(times)

# 5. Primeiras perguntas
print("\nResultados (proporção):")
print(df["resultado"].value_counts(normalize=True).round(3))

print("\nMédia de gols por jogo, por ano:")
print(df.groupby("ano")["gols_total"].mean().round(2))