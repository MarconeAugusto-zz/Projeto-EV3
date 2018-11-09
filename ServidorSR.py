#!/usr/bin/env python3
# coding: utf-8
import threading
import time

from ev3dev.ev3 import *
import socket
import Pyro4

# SERVIDOR DO SR

@Pyro4.expose
class ServidorSR:

    def getEndMAC(self):
        mac = ""
        with open('/sys/class/net/bnep0/address', 'r') as f:
            mac = f.readline().rstrip()
        f.close()
        return mac


    def setCorLed(self, cor):
        if cor == 1:
            Leds.set_color(Leds.LEFT, Leds.YELLOW)
            Leds.set_color(Leds.RIGHT, Leds.YELLOW)
        elif cor == 2:
            Leds.set_color(Leds.LEFT, Leds.RED)
            Leds.set_color(Leds.RIGHT, Leds.RED)
        else:
            Leds.set_color(Leds.LEFT, Leds.GREEN)
            Leds.set_color(Leds.RIGHT, Leds.GREEN)
        return "Teste"

    def setDirecaoManual(self):
        ns = Pyro4.locateNS(Controle.get_ip())
        uri = ns.lookup("dirManual")
        print(uri)
        a = Pyro4.Proxy(uri)
        a.setDirecaomanual()          #Invoca a função no cliente SR, com execução no SS


#############################################################################################################################
class Controle(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def registroServico(self):
        print("Registrando a classe Servidor no servidor de nomes")
        with Pyro4.Daemon(Controle.get_ip()) as daemon:
            # daemon = Pyro4.Daemon(get_ip())
            ns = Pyro4.locateNS(Controle.get_ip())
            uri = daemon.register(ServidorSR)
            ns.register('ServidorSR', uri)
            print("Classe Servidor registarda")
            print(uri)
            daemon.requestLoop()

    def run(self):
        print("Starting ", self.threadID)
        print("ID", self.threadID)
        if self.threadID == 1:
            Controle.registroServico(self)
        print("Exiting ", self.threadID)

# Create new threads
thread1 = Controle(1)
# Start new Threads
thread1.start()
time.sleep(2)
##############################################################################################################################