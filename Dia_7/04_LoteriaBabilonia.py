# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

#%%

import random

#%%

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um numero de 1 a 15"))

        except ValueError as err:
            print("entre com um valor valido")
            continue

        if 1<= numero_usuario <=15:
            return numero_usuario

        print("O valor deve estar entre 1 e 15")



def check_numbers(sorteio, usuario):
      
    if usuario == sorteio:
        print("parabens")
        return True

    elif usuario > sorteio:
        print("numero muito alto")
        return False
    
    else:
        print("numero muito baixo")
        return False








numero_sorteio = random.randint(1,15)
numero_tentativas = 3

for i in range(numero_tentativas):
    
    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
      print("Suas tentativas acabaram")