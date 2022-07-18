#importar biblioteca para limpar a tela a cada print das notas
from os import system
"""
Objetivo do programa é ler valor dentro de um cofre, ler as retiradas,
a cada retirada é mostrada o minímo de notas sacadas, o valor de retirada
não pode passar do valor dentro do cofre, e a cada retirada ele exibe a quantidade
restante no cofre, termina quando retirada for menor ou igual a zero ou quando cofre ficar vazio.
Email: jeangondorek73@gmail.com
Nome: Jean Carlos Canova Gondorek
"""

#variavel auxiliar para contar notas
retiradaauxiliar=0
int(retiradaauxiliar)

#contador de notas
cinco=0
dez=0
vinte=0
cinquenta=0
cem=0
int(cinco)
int(dez)
int(vinte)
int(cinquenta)
int(cem)
#fim contador de notas

#somar todas as retiradas
soma_retiradas=0
int(soma_retiradas)

#ler valor do cofre
valor_cofre=int(input("Digite o valor contido no cofre: "))

#print informando as notas
print("Só trabalhamos com notas de 5, 10, 20, 50 e 100 R$. ")

#ler valor da retirada
valor_retirada=int(input("Digite o valor da retirada: "))

#laço para realizar retiradas
while valor_retirada>0:

    #a cada execução necessário zerar as quantidades de notas
    cinco=0
    dez=0
    vinte=0
    cinquenta=0
    cem=0

    #para o usuário não digitar valor que não tenha as notas, cai no else
    if valor_retirada%5==0:

        #para não poder sacar valor maior do que o disponível
        if valor_cofre>=valor_retirada:
            valor_cofre-=valor_retirada #novo valor do cofre
            soma_retiradas+=valor_retirada #soma de retiradas

            #print do novo valor do cofre, no caso, valor ainda disponível para saque
            print()
            # 0:.2f para printar o .00
            print("Novo valor do cofre {0:.2f} R$. ".format(valor_cofre))

            #código para contagem de notas
            retiradaauxiliar=valor_retirada

            #contagem de notas de 100
            if retiradaauxiliar>=100:
                cem=int(retiradaauxiliar/100)
                retiradaauxiliar=retiradaauxiliar-(cem*100)

            #contagem de notas de 50
            if retiradaauxiliar>=50:
                cinquenta=int(retiradaauxiliar/50)
                retiradaauxiliar=retiradaauxiliar-(cinquenta*50)

            #contagem de notas de 20
            if retiradaauxiliar>=20:
                vinte=int(retiradaauxiliar/20)
                retiradaauxiliar=retiradaauxiliar-(vinte*20)

            #contagem de notas de 10
            if retiradaauxiliar>=10:
                dez=int(retiradaauxiliar/10)
                retiradaauxiliar=retiradaauxiliar-(dez*10)

            #contagem de notas de 5
            if retiradaauxiliar>=5:
                cinco=int(retiradaauxiliar/5)
                retiradaauxiliar=retiradaauxiliar-(cinco*5)

            #print das notas contadas
            print()
            print("--------NOTAS--------")
            print("R$ 100,00 -",cem)
            print("R$ 50,00  -",cinquenta)
            print("R$ 20,00  -",vinte)
            print("R$ 10,00  -",dez)
            print("R$ 05,00  -",cinco)
            print()
            # 0:.2f para printar o .00
            print("Valor que ainda pode ser sacado {0:.2f} R$. ".format(valor_cofre))

        #caso valor seja maior do que o do cofre
        else:
            print("Não é possível sacar este valor! ")
            # 0:.2f para printar o .00
            print("Valor que ainda pode ser sacado {0:.2f} R$. ".format(valor_cofre))

    #caso usuário tenha digitado valor que não haja notas para saque
    else:
        print("Não é possível sacar este valor! ")
        # 0:.2f para printar o .00
        print("Valor que ainda pode ser sacado {0:.2f} R$. ".format(valor_cofre))

    #caso cofre fique vazio, o programa termina automaticamente
    if valor_cofre==0:
        print()
        print("Cofre vazio. ")
        # 0:.2f para printar o .00
        print("Valor de todas as retiradas {0:.2f} R$ ".format(soma_retiradas))
        print("Fim do programa.")
        exit()

    #quebra de linha
    print()

    #lendo valor novamente para nova operação
    valor_retirada=int(input("Digite o valor da retirada: "))
    system("clear")

#print final de valor no cofre e soma de retiradas
# 0:.2f para printar o .00
print("Valor final do cofre {0:.2f} R$. ".format(valor_cofre))
print("Valor de todas as retiradas {0:.2f} R$ ".format(soma_retiradas))
print("Fim do programa.")
