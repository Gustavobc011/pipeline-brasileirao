"""Roda o pipeline: Extrair -> Transformar (Carregar vem na próxima etapa)."""
from pathlib import Path
import pandas as pd

from src.extract import extrair
from src.transform import transformar

SAIDA = Path("data/processed/jogos.csv")


def main():
    caminho_bruto = extrair()                  # E: baixa o CSV
    df_bruto = pd.read_csv(caminho_bruto)      # lê o arquivo baixado
    df_tratado = transformar(df_bruto)         # T: limpa e enriquece

    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    df_tratado.to_csv(SAIDA, index=False)
    print(f"{len(df_tratado)} jogos tratados salvos em {SAIDA}")


if __name__ == "__main__":
    main()