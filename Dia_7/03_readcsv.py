#%%


import math as mh

#%%
arquivo = "Dia_7/dta.csv"

with open(arquivo) as open_file:
    lines = open_file.readlines()


for l in lines:
    print(l)

#%%

dados = dict()

chaves = lines[0].strip("\n").split(";")

for c in chaves:
    dados[c] = []

print(dados)

#%%

for l in lines[1:]:
    valores = l.strip("\n").split(";")

    for i in range(len(valores)):

        dados[chaves[i]].append(valores[i])
dados

#%%

idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
media
