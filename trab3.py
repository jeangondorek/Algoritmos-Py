"""
Jogo PONG desenvolvido em Python utilizando a biblioteca turtle.

Pong é um jogo eletrônico de esporte em duas dimensões que simula
um tênis de mesa. O jogador controla uma paleta (barra vertical)
no jogo movendo-a verticalmente no lado esquerdo da tela, e compete
contra o computador ou outro jogador que controlam uma segunda
raquete no lado oposto. Os jogadores usam suas paletas para
acertar a esfera (bola) e mandá-la para o outro lado. A bola
aumenta de velocidade cada vez que é rebatida, reiniciando a
velocidade caso algum dos jogadores não acerte a bola. O objetivo
é fazer mais pontos que seu oponente, fazendo com que o oponente
não consiga retornar a bola para o outro lado.

Email: jeangondorek73@gmail.com
Email: saintfelixp@yahoo.com
Nome: Pierre Leadny Saint Felix
Nome: Jean Carlos Canova Gondorek
"""

# Bibliotecas para uso no jogo
import turtle
import os
import random
import math
from math import *
from turtle import *
from random import *
from random import randint

## Variaveis Globais ##
# Marcador de pontos para jogador A e B.
pontoa=0
pontob=0
limitep=int(input("Digite o limite de pontos: "))
# Leio antes por não querer ler dentro do turtle
# Limite de pontos, vencedor é o que chega nesse limite

ydoa=-22 ## posição no eixo y, como só mexe nesse eixo
ydob=-22 ## so mexo com essa variavel para cada jogador

tracer(False)##Remove animação

## Variaveis para criar as paletas dos jogadores
cursor = 20
playerheight = 60
playerwidth = 20
####

## Execuções das funções e código principal ##
# Definindo tamanho de tela.
tela = turtle.Screen()    # Acessa o controle da tela (quadro de desenho)
tela.setup(width=1.0, height=1.0 )# Define para tela cheia

# Define a cor de fundo da janela como preta
wn = turtle.Screen()        # Cria o campo para mudar a cor
wn.bgcolor("black")         # Define a cor do campo, igual a todo o fundo, como preto

# Criando caneta
pen3 = turtle.Turtle()        # Cria a caneta
pen3.color("white")      # Define a cor da caneta
pen3.pensize(3)      # Define a espessura da caneta

# Caneta uso exclusivo do score
pen6 = turtle.Turtle()        # Cria a caneta

# Para avisar onde clicar para começar o jogo
pen8 = turtle.Turtle()
pen8.pensize(5)
pen8.penup()
pen8.setposition(-130,270)
pen8.pendown()
pen8.color("white")
pen8.write("Y para começar.",font=("Helvetica",24))
pen8.penup()
pen8.setposition(-1150,1050) # Para tirar da tela a caneta

###JogadorA
pen1 = Turtle("square")       # Cria a caneta que é a paleta
pen1.penup()
pen1.turtlesize(playerheight / cursor, playerwidth / cursor)
pen1.color("blue")      # Define a cor da caneta
pen1.setposition(-450,ydoa) # Posição inicial
###Jogadorb
pen2 = Turtle("square")        # Cria a caneta que é a paleta
pen2.penup()
pen2.turtlesize(playerheight / cursor, playerwidth / cursor)
pen2.color("red")      # Define a cor da caneta
pen2.setposition(450,ydob) # Posição inicial

## Funções ##
# Linha divisória do meio
def divisao():
    tracer(False)##Remove animação
    linha=0
    tl=243
    pen3.left(90)
    while linha<18:
        pen3.penup()
        pen3.color("white")
        pen3.setposition(0,tl)
        pen3.pensize(1)
        pen3.pendown()
        pen3.forward(10)
        tl-=30
        linha+=1

# Criando os limites do campo e desenhando eles
def limite():
    tracer(False)##Remove animação
    pen3.pensize(10)
    pen3.penup()
    pen3.setposition(-800,253)
    pen3.pendown()
    pen3.color("white")
    pen3.forward(1600)
    pen3.penup()
    pen3.setposition(-800,-268)
    pen3.pendown()
    pen3.forward(1600)

# Vê qual tem mais pontos e declara o vencedor
def vencedor():
    tracer(False)##Remove animação
    global pontoa
    global pontob
    global limitep
    pen3.pensize(5)
    pen3.penup()
    pen3.setposition(-80,-20)
    pen3.pendown()
    pen3.color("gold")
    if pontoa>=limitep:
        pen3.write("Jogador A venceu !!!",font=("Helvetica",14,"bold"))
    if pontob>=limitep:
        pen3.write("Jogador B venceu !!!",font=("Helvetica",14,"bold"))
    pen3.penup()
    pen3.setposition(-11180,-11120)
# Definindo pontuação de cada jogador em um placar
def score():
    tracer(False)##Remove animação
    pen6.clear()
    pen6.penup()
    pen6.setposition(-180,-320)
    pen6.pendown()
    pen6.color("white")
    pen6.write("  {}     :: SCORE ::     {}".format(pontoa,pontob),font=("Helvetica",26))
    pen6.penup()
    pen6.setposition(-1180,-1320)# tira caneta da tela

def mostralados():
    tracer(False)##Remove animação
    pen7 = turtle.Turtle()        # Cria a caneta
    pen7.color("white")      # Define a cor da caneta
    pen7.pensize(3)      # Define a espessura da caneta
    pen7.penup()
    pen7.setposition(-450,270) # Posição inicial
    pen7.pendown()
    pen7.write("JOGADOR A",font=("Arial",14,"bold"))
    pen7.penup()
    pen7.setposition(350,270) # Posição inicial
    pen7.pendown()
    pen7.write("JOGADOR B",font=("Arial",14,"bold"))
    pen7.penup()
    pen7.setposition(11111,11111)

# Cria a paleta jogador A
def jogador_a():
    global ydoa
    pen1.pensize(3)      # Define a espessura da caneta
    pen1.penup()
    pen1.setposition(-450,ydoa) # Posição inicial

# Cria paleta jogador B
def jogador_b():
    global ydob
    pen2.pensize(3)      # Define a espessura da caneta
    pen2.penup()
    pen2.setposition(450,ydob) # Posição inicial

##Quando clica w
def onw():
    global ydoa
    global ondejogador1
    global ondejogador2
    if ydoa<218:
        ydoa+=30
    jogador_a()
##Quando clica s
def ons():
    global ydoa
    global ondejogador1
    global ondejogador2
    if ydoa>-218:
        ydoa-=30
    jogador_a()
##Quando clica UP
def onUp():
    global ydob
    global ondejogador1
    global ondejogador2
    if ydob<208:
        ydob+=30
    jogador_b()
##Quando clica DOWN
def onDown():
    global ydob
    global ondejogador1
    global ondejogador2
    if ydob>-218:
        ydob-=30
    jogador_b()
##Quando o jogo começa e a bola se mexe
def start():
    tracer(True)##Coloca animação
    speedball=1
    global pontoa
    global pontob
    global limitep
    global ydoa
    global ydob
    global bola
    global pen1
    global pen2
    bola.setposition(0,0)
    bola.speed(speedball)#### VARIAVEL de velocidade da bola
    x=430
    x1=[430,-430]
    y=0
    i=randint(0,1)
    bola.goto(x1[i],y)
    y=238
    while pontoa<limitep or pontob<limitep:
        for j in range(30):
            if bola.ycor()+j == pen2.ycor() or bola.ycor()-j==pen2.ycor():
                x=(430*2)
                bola.goto(x,y)
                speedball+=1
                break
            elif bola.ycor()+j != pen2.ycor() or bola.ycor()-j!=pen2.ycor():
                x=-470
                bola.goto(x,y)
                speedball+=1
                break
            else:
                x=-470
                bola.goto(x,y)
                speedball+=1
                break
        for j in range(30):
            if bola.ycor()+j == pen1.ycor() or bola.ycor()-j==pen1.ycor():
                x=-(430*2)
                bola.goto(x,y)
                speedball+=1
                break
            elif bola.ycor()+j != pen1.ycor() or bola.ycor()-j!=pen1.ycor():
                x=-470
                bola.goto(x,y)
                speedball+=1
                break
            else:
                x=+470
                bola.goto(x,y)
                speedball+=1
                break
        if y==238:
            y=-252
            speedball+=1
        if y==-252 and x<-256:
            y=238
            speedball+=1
        if x > 451 and pontoa<limitep:
            pontoa+=1
            score()
            speedball=1
            bola.home()
            break
        if x < -451 and pontob<limitep:
            pontob+=1
            speedball=1
            score()
            bola.home()
            break
        if pontoa==limitep or pontob==limitep:
            break
    vencedor()
## Fim ##

tracer(True)

# Executa as funções de criação do campo de jogo, placar e afins
mostralados()
limite()
divisao()
score()
## Cria a bola ## Bola é uma caneta
bola = turtle.Turtle()
bola.penup()
bola.shape("circle")
bola.color("green")

# Código que faz o jogo rodar, ocorrer o jogo com interação de jogadores reais
# E manuseio de funções já criadas
#espernado usuário digitar y para começar o jogo, e após os player mexer suas devidas paletas
turtle.listen()
turtle.onkey(start,"y")
turtle.onkey(onw,"w")
turtle.onkey(onUp,"Up")
turtle.onkey(ons,"s")
turtle.onkey(onDown,"Down")
tracer(False)

# Final, onde ele mostra a mensagem de fechar e após ter mostrado o vencedor
pen3.pensize(5)
pen3.penup()
pen3.setposition(-190,330)
pen3.pendown()
pen3.color("white")
pen3.write("Clique na tela para fechar.",font=("Helvetica",24))
pen3.penup()
pen3.setposition(-1150,1550) # Para tirar da tela a caneta
tela.exitonclick() #A tela será fecha quando houver um clique
