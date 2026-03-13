#%%

#Pares de caves sempre CHAVE:VALOR

dados_pedro = {"Nome":"Pedro", 
               "Idade":21,
               "Formacao": ["Economista", "Analise de dados"],
               "Cargos": [
                   {"Nome": "ds jr.", "empresa": "tapps" },
                   {"Nome": "ds pl.", "empresa": "sas" },
                   {"Nome": "ds sr.", "empresa": "boticario" },
                   {"Nome": "ds espec.", "empresa": "via varejo" },
               ]      
}

print(dados_pedro)

# %%
#Descobrir o valor de uma chave
#Pode ser usado texto ou numero como chave

print(dados_pedro["Nome"])

print(dados_pedro["Idade"])

print(dados_pedro["Formacao"][0])

print(dados_pedro["Cargos"][-1]["empresa"])
# %%

dados_pedro["estado civil"]="solteiro"

print(dados_pedro)

# %%

print(dados_pedro.keys())

print(dados_pedro.values())

print("items", dados_pedro.items())
# %%

for i in dados_pedro:
    print(i, "->", dados_pedro[i])


# %%
for [chave, valor] in dados_pedro.items():
    print(chave, "->", valor)