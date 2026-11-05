"""Etapa 1 do ETL: Extrair (baixar o CSV bruto)."""
from pathlib import Path
import requests

# Cole aqui o link "Raw" do CSV que você encontrou no GitHub
URL = "https://raw.githubusercontent.com/adaoduque/Brasileirao_Dataset/refs/heads/master/campeonato-brasileiro-full.csv"
DESTINO = Path("data/raw/brasileirao.csv")


def extrair(url: str = URL, destino: Path = DESTINO) -> Path:
    """Baixa o CSV e salva em data/raw. Retorna o caminho do arquivo."""
    destino.parent.mkdir(parents=True, exist_ok=True)  # cria a pasta, se faltar
    resposta = requests.get(url, timeout=30)            # faz o download
    resposta.raise_for_status()                         # dá erro se o download falhar
    destino.write_bytes(resposta.content)               # grava o arquivo
    print(f"Arquivo salvo em {destino}")
    return destino


if __name__ == "__main__":
    extrair()