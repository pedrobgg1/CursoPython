# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
 

texto = """Escolha a sua água para comprar

(1) Água mineral natural - R$1,50
(2) Água mineral com gás - R$2,50

"""
opcao = input(texto)

Valor = 0
if opcao == "1":
    Valor = 1.5
elif opcao == "2":
    Valor = 2.5

if Valor == 0:
     print("Escolha uma opção de água valida")

else:
    Qnt = int(input("Escolha a quantidade de garrafas de água que deseja comprar: "))
    Total = Valor*Qnt
    print("Sua conta deu: R$", Total)


# ----------------------------
# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

texto = """
Escolha seu tipo de sorvete:
(1) Casquinha - R$1,00 
(2) Cascão - R$2,50 
(3) Cestinha - R$4,00 
"""
tipos = input(texto)

ValorTipo = 0
Tipo = ""
if tipos == "1":
    ValorTipo = 1.00
    Tipo = "Casquinha"

elif tipos == "2":
    ValorTipo = 2.50
    Tipo = "Cascão"

elif tipos == "3":
    ValorTipo = 4.00
    Tipo = "Cestinha"

if ValorTipo == 0:
    print("Escolha uma opção valida")

else:
    texto2 = """
    Escolha seu sabor de sorvete:
    (1) Morango 
    (2) Creme 
    (3) Chocolate
    """
    sabores = input(texto2)

    Sabor = ""
    if sabores == "1":
        Sabor = "Morango"
    elif sabores == "2":
        Sabor = "Creme"
    elif sabores == "3":
        Sabor = "Chocolate"
    if Sabor == "":
        print("Escolha uma opção valida")
    else:
        texto3 = """
        Escolha sua cobertura de sorvete:
        (1) Caramelo - R$1,50
        (2) Morango - R$1,50
        (3) Chocolate - R$1,50
        (4) Sem Cobertura - R$0,00
        """
        coberturas = input(texto3)

        valorcobertura = 0
        Cobertura = ""

        if coberturas == "1":
            Cobertura = "Caramelo"
            valorcobertura = 1.50

        elif coberturas == "2":
            Cobertura = "Morango"
            valorcobertura = 1.50

        elif coberturas == "3":
            Cobertura = "Chocolate"
            valorcobertura = 1.50

        elif coberturas == "4":
            Cobertura = "Sem Cobertura"
            valorcobertura = 0

        if Cobertura == "":
            print("Escolha uma opção valida")
        else:

            ValorTotal = ValorTipo + valorcobertura

            print("O tipo de sorvete escolhido foi",Tipo,",com sabor de",Sabor,",e cobertura de",Cobertura,",o valor total ficou: ",ValorTotal)


#%%


texto = """
Escolha seu tipo de sorvete:
Casquinha - R$1,00 
Cascão - R$2,50 
Cestinha - R$4,00 
"""
tipos = input(texto)
tipos = tipos.lower()

texto2 = """
Escolha seu sabor de sorvete:
Morango 
Creme 
Chocolate
    """
sabores = input(texto2)
sabores = sabores.lower()

texto3 = """
Escolha sua cobertura de sorvete:
Caramelo - R$1,50
Morango - R$1,50
Chocolate - R$1,50
Sem Cobertura - R$0,00
"""
coberturas = input(texto3)
coberturas = coberturas.lower()

valor = 0

if tipos == "casquinha":
    valor += 1
elif tipos == "cascão":
    valor += 2.5
elif tipos == "cestinha":
    valor += 4

if coberturas in ["caramelo", "morango", "chocolate"]:
    valor += 1.5

txt = f"Seu sorvete {tipos}, de {sabores} com cobertura de {coberturas} custou R${valor:.2f}"
print(txt)


#%%
# Faça um programa que verifique se a pessoa pertence a familia "calvo"

nome = input()
nome_split = nome.lower().split()
if "calvo" in nome_split: # pedro baggio -> ["pedro", "baggio"]
    print("pertence")
else:
    print("nao pertence")


