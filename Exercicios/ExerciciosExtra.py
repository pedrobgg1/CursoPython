#%%
# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Escolha UMA palavra: ").lower()

count = 0

for i in palavra:
    if i == "a":
        count += 1

# ou 

for i in palavra:
    count += int(i == "a") # esta convertendo o false e true para 1 e 0 

# ou
 
count = palavra.count("a")

print(count)

# ----------------------------------------------------------------------------------------------------
# %%
# Escreva um programa que receba o nome de uma pessoa e faça uma saudação.

nome = input("Qual o seu nome?: ")

print("Ola", nome, "! Boas vindas")

# ----------------------------------------------------------------------------------------------------
# %%

nome = input("Qual o seu nome?: ")

idade = input("E qual a sua idade?: ")


print("Ola", nome, "Bom saber que voce tem", idade, "anos.")

# ----------------------------------------------------------------------------------------------------
# %%
# Faça um programa que receba dois valores A e B. 
# Faça a soma desses dois valores e retorne o resultado:


numero = 0
qntnum = 2
for i in range(qntnum):
    num = input("Insira o numero desejada: ")
    num = float(num)
    numero += num

print("A soma dos numeros é", numero)

# ----------------------------------------------------------------------------------------------------
#%%
# Faça um programa que receba dois valores A e B. 
# Faça a potência desses dois valores e retorne o resultado:

num1 = input("Insira o numero desejado: ")
num2 = input("Insira o numero desejado: ")

num1 = float(num1)
num2 = float(num2)

print(num1, "^", num2, "=", num1 ** num2)

# ----------------------------------------------------------------------------------------------------
#%%

# Faça um programa que receba o raio de uma circunferência em centímetros.
# Retorne para o usuário qual é a área e perímetro desta circunferência

raio = input("Insira o valor do raio: ")
raio = int(raio)

area = (3.14*(raio**2))
area = float(area)
area = round(area,2)


perimetro = (2*3.14)*raio
perimetro = float(perimetro)
perimetro = round(perimetro,2)

print("A área do circulo é: ", area)
print("O perimetro do circulo é: ", perimetro)

# ----------------------------------------------------------------------------------------------------
#%%
# Faça um programa que receba um número em segundos, 
# # converta esse número para horas, minuto e segundos.

# segundos = input()
# segundos = int(segundos)



# minutos = segundos/60
# minutos = float(minutos)
 
# if minutos >=60:
#     minutos = minutos - 60



# horas = segundos/3600
# horas = float(horas)

# print(segundos, minutos, horas)

# ----------------------------------------------------------------------------------------------------
#%%

number = input()
number = int(number)

resto = number % 2
resto

if resto == 1:
    print("O numero: ", number, ", é impar")
else:
    print("O numero: ", number, ", é par")

# ----------------------------------------------------------------------------------------------------
#%% 
# Escreva um programa que solicite ao usuário um nome e uma idade, e crie um dicionário com essas informações. 
# Em seguida, exiba o dicionário.

nome = input("Nome: ")
idade = input("Idade: ")

dic = {"Nome":nome,
       "Idade": idade}
print(dic)

# ----------------------------------------------------------------------------------------------------
#%%
# Faça um programa que receba 4 notas de um aluno. 
# Retorne a média dessas notas, a menor e a maior nota:


notas = []
qntnotas = 4
for i in range(qntnotas):
    nota = input("Adicione uma nota: ")
    notas.append(float(nota))

med = sum(notas) / qntnotas
minimo = min(notas)
maximo = max(notas)

print("Media", med)
print("Maximo", maximo)
print("Minimo", minimo)

# ----------------------------------------------------------------------------------------------------
#%%
# Faça um programa que retorne as seguintes informações:
# Elemento na posição -1 da lista
# Elemento na primeira posição da lista
# O último caractere do segundo elemento da lista

lista = [120, "Python", 120.01, "asw", False, [10,20]]


print(lista[-1])
print(lista[0])

for i in lista[1]:
    if i == lista[1][-1]:
        print("Ultima letra:",i)

# ----------------------------------------------------------------------------------------------------
#%%
# Escreva um programa que solicite ao usuário duas strings e as concatene em uma única String. 
# Em seguida, exiba a String resultante.

frase = []
qntfrase = 2

for i in range(qntfrase):
    choice = input("Frase da sua escolha: ")
    frase.append(choice)

print(frase)

# ----------------------------------------------------------------------------------------------------
#%%
# Faça um programa com uma função que recebe uma frase. Para cada palavra nesta frase, 
# inverta a ordem das letras. 
# Exiba o resultado


# frases = []

# choice = input("frase: ")

# for i in choice:
#     frases

# ----------------------------------------------------------------------------------------------------