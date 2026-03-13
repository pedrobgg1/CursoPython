#%%
import requests

import json

from tqdm import tqdm

import pandas as pd
#%%

ceps = ["01519000",
        "80250200",
        "85640000",
        "21051090"
]



url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados


#%%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")


#%%
print(dados)

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
