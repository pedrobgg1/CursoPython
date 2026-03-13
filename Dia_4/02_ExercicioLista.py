
# Escreba um programa que receba uma lsita de numero
# do usuario e conte quantas vezes um numero
# especifico aparece na lista
# Solicite ao usuario um numero e exiba a contagem


#%%
lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = input("Entre com um numero: ")
numero = int(numero)

contador = 0

for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, ":", contador)

# %%

idades = []

while True:
    idade = input("entre com a idade: ")

    if idade == "":
        break
    
    idades.append(int(idade))

media = sum(idades)/len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTDE:", qtde)

print(idades)
