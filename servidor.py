#devemos utilizar semaforos pra fazer bloqueante??
#criar um servidor http e fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket

porta   = 8080
bufferSize  = 1024
msgFromServer = "Cliente conectado ao servidor"
bytesToSend = str.encode(msgFromServer)

def atividadeTS(comando): #Definicao do recebimento de atividade no servidor pelo cliente???
	if comando == 'out':
		print('OLHA AI MENINA')
		return		
	if comando == 'in' :
		return
	if comando == 'rd' :
		return
	else:
		return False

socketservidor = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	# Cria o socket para comunicacao
socketservidor.bind(('', porta))		# Une o cliente ao socket servidor
#socketservidor.listen(5)
print("Servidor disponivel")

while(True):
    bytesAdrPar = socketservidor.recvfrom(bufferSize)
    mensagem = bytesAdrPar[0]
    adr = bytesAdrPar[1]
    clientMsg = "Message from Client:{}".format(mensagem)
    clientIP  = "Client IP Address:{}".format(adr)
    atividadeTS(mensagem)
    socketservidor.sendto(bytesToSend, adr)