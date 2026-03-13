#%%

import requests
import pandas as pd

#%%


url = "https://ddragon.leagueoflegends.com/cdn/16.4.1/data/en_US/champion.json"

resp = requests.get(url)

df = pd.DataFrame(resp.json())


#%%
df.to_csv("champs_lol.csv", sep=";", index =False)



#%%

dt = pd.read_csv("champs_lol.csv")
print(dt.head())