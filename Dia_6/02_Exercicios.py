#%%


def f(num:int):
    if num %2 == 0:
        print("O numero é Par")
    else:
        print("O numero é Impar")

num = input("Entre com um numero: ")
num = int(num)

f(num)

#%%
#estatisticas

#soma

def soma(a:float,b:float)->float:
    return a + b

#media

def media(a:float,b:float)->float:
    return soma(a,b)/2

a = float(input("entre com o valor de A: "))
b = float(input("entre com o valor de A: "))

print("Soma e:", soma(a,b), "A media e: ", media(a,b))


#%%


#soma

def soma(valores:list)->float:
    return sum(valores)

#media

def media(valores:list)->float:
    return soma(valores)/ len(valores)

a = float(input("entre com o valor de A: "))
b = float(input("entre com o valor de B: "))
c = float(input("entre com o valor de C: "))

print("Soma e:", soma([a,b,c]), "A media e: ", media([a,b,c]))



