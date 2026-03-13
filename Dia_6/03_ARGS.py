#%%

# Usando o *args para adicionar valores a list sem precisar mexer nela necessariamente
# Os unicos valores que sao necessarios sao o A e B

#soma

def soma(a:float, b:float, *args)->float:
    valores = [a,b]+list(args)
    return sum(valores)

#media

def media(a:float,b:float, *args)->float:
    return soma(a,b, *args) / (len(args)+2)

a = float(input("entre com o valor de A: "))
b = float(input("entre com o valor de B: "))
c = float(input("entre com o valor de C: "))
d = float(input("entre com o valor de D: "))
e = float(input("entre com o valor de E: "))

print("Soma e:", soma(a,b,c,d,e), "A media e: ", media(a,b,c,d,e))

