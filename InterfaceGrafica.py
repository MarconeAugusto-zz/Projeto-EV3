#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import threading
import time
import Pyro4
from projetoRobo.ClienteSR import ClienteSR

class Packing:

    def __init__(self, instancia_Tk):
        self.fontePadrao = ("Arial", "20")
        self.texto = StringVar()

        self.container1 = Frame(instancia_Tk)
        self.container2 = Frame(instancia_Tk)
        self.container3 = Frame(instancia_Tk)
        self.container4 = Frame(instancia_Tk)
        self.container5 = Frame(instancia_Tk)
        self.container6 = Frame(instancia_Tk)
        self.container7 = Frame(instancia_Tk)
        self.container8 = Frame(instancia_Tk)
        self.container9 = Frame(instancia_Tk)
        self.container10 = Frame(instancia_Tk)
        self.container11 = Frame(instancia_Tk)

        #adicionando os containers
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        self.container4.pack()
        self.container5.pack()
        self.container6.pack()
        self.container7.pack()
        self.container8.pack()
        self.container9.pack()
        self.container10.pack()
        self.container11.pack()

        #adicionando os botões aos containers
        self.espaco = Label(self.container1, text='      ', font=self.fontePadrao, pady="20").pack()
        self.b1 = Button(self.container2, text='Frente',font=self.fontePadrao, command=self.frentePressionado, bg="gray", width=20).pack()
        self.b2 = Button(self.container3, text='Esquerda',font=self.fontePadrao, command=self.esquerdaPressionado, bg="gray", width=20).pack(side=LEFT)
        self.b3 = Button(self.container3, text='  Direita  ',font=self.fontePadrao, command=self.direitaPressionado, bg="gray", width=20).pack(side=LEFT)
        self.b4 = Button(self.container4, text= '   Ré   ', font=self.fontePadrao, command=self.rePressionado, bg="gray", width=20).pack()
        self.espaco = Label(self.container5, text='      ', font=self.fontePadrao, pady="50").pack()
        self.b5 = Button(self.container6, text='Valida Caça',font=self.fontePadrao, command=self.validaPressionado, bg="gray", width=20).pack()
        self.b6 = Button(self.container7, text='     Pausa    ', font=self.fontePadrao, command=self.pausaPressionado, bg="gray", width=20).pack()
        self.b7 = Button(self.container8, text=' Fim de jogo', font=self.fontePadrao, command=self.fimPressionado, bg="gray", width=20).pack()
        self.espaco = Label(self.container9, text='      ', font=self.fontePadrao, pady="50").pack()
        self.dados = Label(self.container10, font=self.fontePadrao, textvariable=self.texto, width="50").pack()
        self.espaco = Label(self.container11, text='      ', font=self.fontePadrao, pady="50").pack()


    def frentePressionado(self):
        direcao = 0
        self.texto.set("Movendo para frente...")
        print("Movendo para frente")
        ClienteSR.MovimentoManual(self,direcao)
        #adiconar aqui a implementação do objeto distrído que vai chamar a função move()

    def esquerdaPressionado(self):
        direcao = 1
        self.texto.set("Movendo para esquerda...")
        print("Movendo para esquerda")
        ClienteSR.MovimentoManual(self, direcao)
        #adiconar aqui a implementação do objeto distrído que vai chamar a função move()


    def direitaPressionado(self):
        direcao = 2
        self.texto.set("Movendo para direita...")
        print("Movendo para direita")
        ClienteSR.MovimentoManual(self, direcao)
        #adiconar aqui a implementação do objeto distrído que vai chamar a função move()


    def rePressionado(self):
        direcao = 3
        self.texto.set("Movendo para trás...")
        print("Movendo para trás")
        ClienteSR.MovimentoManual(self, direcao)
        #adiconar aqui a implementação do objeto distrído que vai chamar a função move()


    def validaPressionado(self):
        #adiconar aqui a implementação do objeto distrído que vai chamar a função validaCaca()
        self.texto.set("Validando caça...")
        print("Validando caça")

    def pausaPressionado(self):
        #adiconar aqui a implementação do objeto distrído que vai chamar a função pausa()
        self.texto.set("Jogo pausado")
        print("Jogo pausado")

    def fimPressionado(self):
        #adiconar aqui a implementação do objeto distrído que vai chamar a função fimDeJogo()
        self.texto.set("Finalizando a partida...")
        print("Finalizando a partida...")
        #self.raiz.destroy()

    def IniciaInterface(self,r):
        raiz = r
        raiz.title("Modo Manual")
        print(raiz.title)
        Packing(raiz)
        raiz.mainloop()


class Configuracao(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def run(self):
        print("Starting ", self.threadID)
        print("ID", self.threadID)
        if self.threadID == 3:
            raiz = Tk()
            Packing.IniciaInterface(self,raiz)
        print("Exiting ", self.threadID)

# Create new threads
thread1 = Configuracao(3)
# Start new Threads
thread1.start()
# time.sleep(0.5)