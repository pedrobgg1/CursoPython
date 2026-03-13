#%% 

# KWArgs ao contraria de ser uma lista/tupula como o args ele é um dicionario


def calc_imposto(preco:float, tx_imposto:float, **kwargs):
    imposto = preco * tx_imposto

    for chave in kwargs:
        print(chave,kwargs[chave])
        imposto += preco*kwargs[chave]
    return imposto

#%%

taxas_gerais={
    "municipio":0.01, 
    "estadual":0.005, 
    "nacional":0.001
}

# calc_imposto(preco=100, tx_imposto=0.03, municipio=0.01, estadual=0.005, nacional=0.001)
calc_imposto(preco=100, tx_imposto=0.03, **taxas_gerais)