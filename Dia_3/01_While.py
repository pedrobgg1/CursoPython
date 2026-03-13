#%%
numero = 2
count = 1

while count <= 100:
    print(numero, "X", count, "=", numero*count)
    count = count + 1
print("Finalizado")

#%%
# Numeros divisiveis por 4 no intervalo 4-100

count = 4

while count <= 100:
    sobra = count % 4
    if sobra == 0:
        print(count, "/", 4, "=", int(count/4))

    count += 1