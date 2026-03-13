#%%
idade = 18

if idade >= 18:
    print("Voce pode beber cerveja")
else: print("Voce não pode beber cerveja")


#%%
# ELIF

idade = 80

if idade > 70:
    print("Cuidado com a bebida")
    print("Consulte seu medico")

#Ignora o if se o anterior foi aceito
elif idade >= 18:
    print("Voce pode beber cerveja")
    print("beba com moderação")

else: print("Voce não pode beber cerveja")