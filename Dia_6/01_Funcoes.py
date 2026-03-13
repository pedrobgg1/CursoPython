#%%
valor = input("Entre com um valor")
print(valor)


#%%

def f(x):
    resultado = 1+x
    return resultado

#%%

f(10)


#%%
#Juros compostos

def juros_compostos(aporte:int, taxa:float,anos:int) -> float:
    """ Juros compostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve se considerar o valor, taxa de juros e tempo (em anos).

    aporte:
        Um número inteiro que represente o valor em R$

    Taxa:
        um numero float entre 0 e 1 representando a taxa que sera adicionada ao aporte
    
    Anos:
        Numeros inteiros >= 1 que representam a quantidade de anos que o investimento durara
    """
    return aporte*(1+taxa)**anos

aporte = int(input("Insira o valor do aporte: "))
taxa = float(input("Insira o valor da taxa: "))
anos = int(input("Insira o valor dos anos: "))

print("O valor final do investimento é de: ", juros_compostos(aporte,taxa,anos))



