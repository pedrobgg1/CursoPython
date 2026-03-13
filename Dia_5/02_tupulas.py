#%%
dados_teo = [32,1,"casado", "dev golang"]
dados_teo

# %%
dados_teo.append("3241.43")
dados_teo[0] = 28
dados_teo
# %%
# Tupula é garantir que o objeto é imutavel
# tupula = ()
# Lista = []
# Listas dentro de tupulas sao mutaveis

tupula_teo = (32,1,"casado", "dev golang")

print(type(tupula_teo))
print(tupula_teo)
# %%

tupula_teo[0]=28

#TypeError: 'tuple' object does not support item assignment

