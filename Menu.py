#!/usr/bin/env python3
# coding: utf-8

import subprocess
import threading
import time
import Pyro4
import socket
from time import sleep
from Movimento import *

########################################################################################################################
class controle(threading.Thread):
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

    def startServer(self):
        print("start server")
        Ip = controle.get_ip(self)
        str = "pyro4-ns --host "
        cmd = str + Ip
        print(cmd)
        subprocess.call(cmd, shell=True)

    def run(self):
        print("Starting ", self.threadID)
        print("ID", self.threadID)
        if self.threadID == 1:
            controle.startServer(self)
        print("Exiting ", self.threadID)

##Create new threads
thread1 = controle(1)
##Start new Threads
thread1.start()
time.sleep(18)
########################################################################################################################

mov = Movimento(2)
mov.modoJogo()
