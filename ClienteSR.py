#!/usr/bin/env python3
# coding: utf-8
import threading
import time
import Pyro4

class ClienteSR:
    def setCorLed(self):
        ns = Pyro4.locateNS("10.42.0.79")  # IP do robô
        uri = ns.lookup('ServidorSR')
        print(uri)
        o = Pyro4.Proxy(uri)
        c = input("Informe a cor do led: ")
        cor = int(c)
        print(o.setCorLed(cor))

    def getEndMAC(self):
        ns = Pyro4.locateNS("10.42.0.79")  # IP do robô
        uri = ns.lookup('ServidorSR')
        print(uri)
        o = Pyro4.Proxy(uri)
        print(o.getEndMAC())

    def MovimentoManual(self, direcao):
        ns = Pyro4.locateNS("10.42.0.79")  # IP do robô
        uri = ns.lookup('Movimento')
        print(uri)
        o = Pyro4.Proxy(uri)
        o.move(direcao)

    #
    # # MOVIMENTO USA ESSA FUNÇÃO, MODO MANUAL
    # @Pyro4.expose
    # @Pyro4.callback
    # def setDirecaoManual(self):
    #     print("Iniciando interface gráfica")
    #     #raiz = Tk()
    #     #grafico = InterfaceGrafica(raiz)
    #     #return grafico.desenhar()

########################################################################################################################
# class Callback(threading.Thread):
#     def __init__(self, threadID):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#
#     def registraCallback(self):
#         print("Registrando chamada reversa")
#         daemon = Pyro4.core.Daemon("10.42.0.79")
#         ns = Pyro4.locateNS("10.42.0.79")
#         uri = daemon.register(ClienteSR.setDirecaoManual(self))
#         print(uri)
#         server = ns.register("dirManual", uri)
#         print("Objeto registrado Callback")
#         print(uri)
#         daemon.requestLoop()
#
#     def run(self):
#         print("Starting ", self.threadID)
#         print("ID", self.threadID)
#         if self.threadID == 1:
#             Callback.registraCallback(self)
#         else:
#             ClienteSR.setDirecaoManual(self)
#         print("Exiting ", self.threadID)

# Create new threads
#thread1 = Callback(1)
#thread2 = Callback(2)
# Start new Threads
#thread1.start()
#time.sleep(5)
#thread2.start()
########################################################################################################################