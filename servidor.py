#devemos utilizar semaforos pra fazer bloqueante??
#criar um servidor http e fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket
import json
from main import pack, unpack

porta   = 8080
bufferSize  = 1024
msgFromServer = "Cliente conectado ao servidor"
bytesToSend = str.encode(msgFromServer)
tuple_space = []

def atividadeTS(comando): #Definicao do recebimento de atividade no servidor pelo cliente???
	if comando == 'out':
		print('OLHA AI MENINA')
		return		
	if comando == 'in' :
		print('oloco bixo, caiu no in')
		return
	if comando == 'rd' :
		print('quer ler? vai ler um livro vagabunda')
		return
	else:
		return False

socketservidor = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	# Cria o socket para comunicacao
socketservidor.bind(('', porta))		# Une o cliente ao socket servidor
#socketservidor.listen(5)
print("Servidor disponivel")

while(True):
    bytesAdrPar = socketservidor.recvfrom(bufferSize)
    struct = unpack(bytesAdrPar[0].decode('utf-8'))
    nome = struct['cliente']
    mensagem = struct['operacao']
    #mensagem = mensagem.decode("utf-8")
    adr = bytesAdrPar[1]

    clientMsg = "Message from Client:{}".format(mensagem)
    clientIP  = "Client IP Address:{}".format(adr)
    atividadeTS(mensagem)
    socketservidor.sendto(bytesToSend, adr)