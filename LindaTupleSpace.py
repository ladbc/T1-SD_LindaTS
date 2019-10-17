#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import http.server
import socketserver
import os
import sys
import socket
import json
from main import pack

endrServidor  = ("127.0.0.1", 8080)  #Endereco do servidor
bufferSize    = 1024				 #Tamanho do buffer
defPort       = 8080		         #Porta fixa do servidor

#Secao de menu para facilitar uso da aplicacao pelo cliente 
nomeCliente = input("Qual o seu nome?: \n")
print("Entre com o seu comando: ")
array_options = ["out", "in", "rd"]
option_input = int(input("1 - out \n2 - in \n3 - rd \n => "))

#Coleta de dados a serem enviados para o servidor de acordo com a resposta do cliente
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

#Envio dos dados do usuário
bytesenviar = tupla

#Criacao do socket para envio da informacoes 
socketcliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socketcliente.sendto(bytesenviar, endrServidor)
mensagemservidor = socketcliente.recvfrom(bufferSize)
print(mensagemservidor[0].decode('utf-8'))