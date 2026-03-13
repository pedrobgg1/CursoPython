#%%

# O FOR percorre os elementos de um objeto
# EX: cada letra
nome = "Pedro Baggio"

for letra in nome:
    print(letra)

#%%

numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "X", i, "=", numero*i)

#%%

for i in range(4, 101):
    if i % 4 == 0:
        print(i)

#%%

soma = 0
qnt_entradas = 4
for i in range(qnt_entradas):
    alt = input("Insira a altura desejada: ")
    alt = float(alt)
    soma += alt

print("A soma das alturas é", soma)
