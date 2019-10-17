#devemos utilizar semáforos pra fazer bloqueante??
#criar um servidor http é fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket

defPort = 8080

#Definição do cliente do micro-blog   
class Client():
  def __init__(self, addr: tuple):
      self.__socket = socket.socket()
      self.__socket.connect(addr)

  def close(self):
      self.__socket.close()

  def out_tuple(self, topico, menssagem):    #Operação de inserção no tuple space
    #Postagem de conteúdo por tópicos
    Servidor.atividade

  def in_tuple(self, topico, menssagem):     #Operação de retirada no tuple space BLOQUEANTE
    #Retirada de conteúdo somente por quem postou
    print("ai")
    
  def rd_tuple(self, topico):     #Operação de cópia do template de tupla no tuple space BLOQUEANTE
    #Obtenção de conteúdo por tópicos
    print("ai")