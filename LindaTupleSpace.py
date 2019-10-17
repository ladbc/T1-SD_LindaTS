#devemos utilizar semaforos pra fazer bloqueante??
#criar um servidor http e fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket

defPort = 8080

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

mensagemcliente       = "out"
bytesenviar         = str.encode(mensagemcliente)
endrServidor  = ("127.0.0.1", 8080)
bufferSize          = 1024

# Create a UDP socket at client side
socketcliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
socketcliente.sendto(bytesenviar, endrServidor)
mensagemservidor = socketcliente.recvfrom(bufferSize)
msg = "Mensagem do Servidor".format(mensagemservidor[0])
print(msg)