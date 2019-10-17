#devemos utilizar semaforos pra fazer bloqueante??
#criar um servidor http e fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket
import json
from main import pack, unpack

defPort = 8080

def close(self):
	return
def out_tuple(self, topico, menssagem):    #Operacao de insercao no tuple space
  #Postagem de conteudo por topicos
  return
def in_tuple(self, topico, menssagem):     #Operacao de retirada no tuple space BLOQUEANTE
  #Retirada de conteudo somente por quem postou
  print("ai")
  return
def rd_tuple(self, topico):     #Operacao de copia do template de tupla no tuple space BLOQUEANTE
  #Obtencao de conteudo por topicos
  print("ai")
  return

nomeCliente = input("Qual o seu nome?: \n")
print("Entre com o seu comando: ")
array_options = ["out", "in", "rd"]
option_input = int(input("1 - out \n2 - in \n3 - rd \n => "))

message = pack({'operacao': array_options[option_input-1], 'cliente': nomeCliente, 'topic': "topico", 'message': "mensagem"})

mensagemcliente = array_options[option_input-1]
bytesenviar = message
endrServidor  = ("127.0.0.1", 8080)
bufferSize          = 1024

# Create a UDP socket at client side
socketcliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
socketcliente.sendto(bytesenviar, endrServidor)
mensagemservidor = socketcliente.recvfrom(bufferSize)
msg = "Mensagem do SErvidor".format(mensagemservidor[0])
print(msg)