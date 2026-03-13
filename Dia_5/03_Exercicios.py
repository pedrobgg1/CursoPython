
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
#%%

escolha = input("Escolha a fruta desejada: ")

frutas = {"Maçã": "R$1,50",
          "Banana": "R$2,75",
          "Uva": "R$1,90",
          "Pera": "R$1,25",
          "Laranja": "R$0,65",
          "Limão": "R$1,25",
          "Goiaba": "R$2,15",
          "Abacaxi": "R$3,20",
          "Jaca": "R$5,80"
}


if escolha in frutas:
    print(frutas[escolha])
else:
    print("Escolha uma fruta valida")


# %%
# Escreva um programa que solicite ao usuário frases. 
# Para parar de solicitar frases, ele pode apenas apertar o “enter”.
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.



frases = {}


while True:
    escolha = input("Insira uma frase: ")
    if escolha == "":
        break
    if escolha not in frases:
        frases[escolha] = 1
    else:
        frases[escolha] += 1

for i in frases:
    print(i, "->", frases[i])
# %%

frases = {
    "oi":1,
    "tchau":2,
    "Bye":10,
    "nsei":20,
    "lol":12
}

items = list(frases.items())
items.sort(key=lambda X: X[-1], reverse=True)

for i,j in items:
    print(i, "->",j)