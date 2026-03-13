#%%

# Uma maneira de definir listas - Aceita qualquer tipo de dado (int, float, texto, bool) ao mesmo tempo ou nao
idades = [21, 17 ,52, 32 , 54 , 74 , 23]


print(idades)


# %%


# Pegar um elemento de uma lista, começando com 0
print(idades[2])
print(idades[0])
print(idades[1])
# %%

soma = sum(idades)

print("Soma das Idades:", soma)

qnt = len(idades)
print("Qnt Idades:",qnt)

avg = soma/qnt
print("Media de idades:", avg)

minimo = min(idades)
print("Menor idade:", minimo)

maximo = max(idades)
print("Maior idade", maximo)


# %%

pedro = ["Pedro Baggio",
         21, 
         True, 
         "Solteiro",
         ["CSGO", "ROCKET LEAGUE", "LEAGUE OF LEGENDS", "HEARSTONE","Hollow knight","TBOI","God Of War"],
         ["Ampere","Curitba","Itajai"],
         ["Giovana", "Raphaela", "Kahuany"]]

print(len(pedro))

ex = pedro[4]
primeira_ex = ex[0]
print(primeira_ex)

# %%

print(pedro[len(pedro)-1])

# OU

pedro[-1][-2]

# %%
# FATIAMENTO
# Lembrando que começa no 0 e termina no 4 nao pegando o quinto elemento
pedro[0:4]

# %%

# 2 ultimos elementos de jogos

pedro[4][2:4]

# OU

pedro[4][-2:]

# Ou

jogos = pedro[4]
jogos [2:4]

# %%

#Trocar a ordem - TRas para frente

jogos = pedro[4]
print(jogos)
print(jogos[::-1])

# 2 em 2

print(jogos[::2])
