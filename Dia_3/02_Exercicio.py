
#%%
# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma = 0
qnt_entradas = 4
while qnt_entradas > 0:
    alt = input("Insira a altura desejada: ")
    alt = float(alt)
    soma += alt
    qnt_entradas -= 1

print("A soma das alturas é", soma)


#%%

# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, 
# mas quando o usuário apertar “enter” sem digitar valor algum, 
# o programa para de receber valores, e exibe a soma de todos os valores digitados anteriormente.


saldo_total = 0
valor = ""

while True:
    saldo = input("Insira o saldo em conta: ")
    if saldo == "":
        break
    saldo = float(saldo)
    saldo_total += saldo
print(saldo_total)

