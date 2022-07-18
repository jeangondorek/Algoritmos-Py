"""
Objetivo do programa é ler vaor do produto e parcelas e fazer com que o programa
retorne o valor total do produto, o número de parcelas e o valor de parcelas.
Programa que auxiliará um vendedor.
Email: jeangondorek73@gmail.com
Nome: Jean Carlos Canova Gondorek
"""
valordoproduto=float(input("Digite o valor do produto: "))
parcelas=int(input("Digite o número de parcelas: "))
#variável para fazer valor da parcela
valor=valordoproduto
#1 parcela
if parcelas==1:
    #maior que 300 e menor igual que 500
    if valor>=300 and valor<500:
        valordoproduto=valordoproduto-(valordoproduto*0.1)
        valor=valordoproduto
    #maior que 500
    elif valor>=500:
        valordoproduto=valordoproduto-(valordoproduto*0.25)
        valor=valordoproduto
    #menor que 300
    else:
        valordoproduto=valor
        valor=valordoproduto
#2 parcelas
if parcelas==2:
    valor=valordoproduto/parcelas
#3 parcelas
elif parcelas==3:
    #menor que 1100
    if valordoproduto<=1100:
        valordoproduto=valordoproduto+(valordoproduto*0.1)
        valor=valordoproduto/parcelas
    #maior que 1100
    else:
        valordoproduto=valordoproduto+(valordoproduto*0.2)
        valor=valordoproduto/parcelas
#4 parcelas
elif parcelas==4:
    valor=valordoproduto/parcelas
#5 parcelas
elif parcelas>=5:
    valordoproduto=valordoproduto+(valordoproduto*0.25)
    valor=valordoproduto/parcelas
#print
print()
print("O preço final é R$ {0:.2f}, parcelado em".format(valordoproduto),parcelas," vez(es) de R$ {0:.2f}.".format(valor))
print()
