"""Exploração inicial: conhecer o arquivo antes de tratar."""
import pandas as pd

pd.set_option("display.max_columns", None)  # mostra todas as colunas
pd.set_option("display.width", 200)         # evita quebrar linhas no terminal

df = pd.read_csv("data/raw/brasileirao.csv")

print("Formato (linhas, colunas):", df.shape)
print("\nColunas:", list(df.columns))
print("\nPrimeiras linhas:")
print(df.head())
print("\nTipos e valores preenchidos:")
df.info()
print("\nValores faltando por coluna:")
print(df.isna().sum())