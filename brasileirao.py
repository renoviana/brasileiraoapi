import requests
from classes import Brasileirao, Classificacao, Rodada, ListaJogo
from bs4 import BeautifulSoup
import re
import json
soup = BeautifulSoup(requests.get(
    "https://globoesporte.globo.com/futebol/brasileirao-serie-b/").text, 'html.parser')

data = json.loads(re.search(r"classificacao = (.*?);",
                            soup.find("script", {"id": "scriptReact"}).text).group(1))
data_artilheiros = soup.find("section", {"class": "artilharia-wrapper"}
                             ).find_all("div", {"class": "jogador"})
data["artilheiros"] = [{"time": jogador.find("div", {"class": "jogador-escudo"}).find("img")['alt'],
                        "nome": jogador.find("div", {"class": "jogador-nome"}).text,
                        "gols": int(jogador.find("div", {"class": "jogador-gols"}).text)
                        } for jogador in data_artilheiros]

brasileirao = Brasileirao.from_dict(data)
