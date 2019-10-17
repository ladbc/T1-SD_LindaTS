#devemos utilizar semaforos pra fazer bloqueante??
#criar um servidor http e fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket
import json
from main import pack

defPort = 8080

nomeCliente = input("Qual o seu nome?: \n")
print("Entre com o seu comando: ")
array_options = ["out", "in", "rd"]
option_input = int(input("1 - out \n2 - in \n3 - rd \n => "))

if array_options[option_input-1] == 'out':
	topico = input("Você escolheu enviar uma mensagem\nQual o topico?: ")
	message = input("Qual a mensagem?: ")
	tupla = pack({'operacao': array_options[option_input-1], 'cliente': nomeCliente, 'topico': topico, 'mensagem': message})
elif array_options[option_input-1] == 'in':
	topico = input("Você escolheu apagar uma mensagem\nQual o topico?: ")
	tupla = pack({'operacao': array_options[option_input-1], 'cliente': nomeCliente, 'topico': topico, 'mensagem': "message"})
elif array_options[option_input-1] == 'rd':
	topico = input("Você escolheu ler uma mensagem\nQual o topico?: ")
	tupla = pack({'operacao': array_options[option_input-1], 'cliente': nomeCliente, 'topico': topico, 'mensagem': "message"})

mensagemcliente = array_options[option_input-1]
bytesenviar = tupla
endrServidor  = ("127.0.0.1", 8080)
bufferSize          = 1024

# Create a UDP socket at client side
socketcliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
socketcliente.sendto(bytesenviar, endrServidor)
mensagemservidor = socketcliente.recvfrom(bufferSize)
print(mensagemservidor[0].decode('utf-8'))