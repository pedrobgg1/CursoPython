
# Faça um programa que dê bom dia;


print("Bom dia")


# Faça um programa que de bom dia, pergunta o nome da pessoa e responde que é um prazer conhecer ela, citando o nome da pessoa.
print("Bom dia")
nome = input("Qual o seu nome?")

print("E um prazer te conhecer,", nome)

# Crie uma história simples. Adicione essa história em um programa. A cada parágrafo, a história deve aguardar o usuário apertar “enter” para dar continuidade.

p1 = "paragrafo 1"
p2 = "paragrafo 2"
p3 = "paragrafo 3"
p4 = "paragrafo 4"

#print(p1)
input(p1)
#print(p2)
input(p2)
#print(p3)
input(p3)
#print(p4)
input(p4)
#%% 
# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = input("Escolha um numero inteiro para descobrir sua raiz quadrada: ")
numero = int(numero)

raiz = numero ** (1/2) # ou numero ** 0,5
#arredondar
raiz = round(raiz, 4)
print("A Raiz quadrada de", numero, "e", raiz)
#%% 
# Faça um programa que exiba o dobro de um número inserido pelo usuário.

numero = input("Escolha um numero inteiro para calcular seu dobro: ")
numero = float(numero)
dobro = numero*2
print("O dobro de", numero, "e", dobro)