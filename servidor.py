#devemos utilizar semaforos pra fazer bloqueante??
#criar um servidor http e fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket
import json
from main import pack

porta   = 8080
bufferSize  = 1024
msgFromServer = "Cliente conectado ao servidor"
bytesToSend = str.encode(msgFromServer)
tuple_space = []

def atividadeTS(comando,nome,topico,mensagem): #Definicao do recebimento de atividade no servidor pelo cliente???
	if comando == 'out':
		tuple_space.append({'cliente': nome, 'topico': topico, 'mensagem': mensagem})
		response = "Mensagem criada"
	elif comando == 'in' :
		i = 0
		while i < len(tuple_space):
			if tuple_space[i]['topico'] == topico:
				if tuple_space[i]['cliente'] == nome:
					tuple_space.pop(i)
					response = "Mensagem apagada"
				else:
					response = "Sem permissão"
			else:
				response = "Topico não encontrado"
			i+=1
	elif comando == 'rd' :
		array_aux = []
		i = 0
		while i < len(tuple_space):
			if tuple_space[i]['topico'] == topico:
				array_aux.append(tuple_space[i])
			i+=1
		if len(array_aux) == 0:
			response = "Sem mensagens nesse topico"
		else:
			response = array_aux
	print(response)
	print("tuple_space atul = ", tuple_space)
	return response

socketservidor = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)	# Cria o socket para comunicacao
socketservidor.bind(('', porta))		# Une o cliente ao socket servidor
#socketservidor.listen(5)
print("Servidor disponivel")

while(True):
    bytesAdrPar = socketservidor.recvfrom(bufferSize)
    struct = unpack(bytesAdrPar[0].decode('utf-8'))
    nome = struct['cliente']
    operacao = struct['operacao']
    topico = struct['topico']
    mensagem = struct['mensagem']
    adr = bytesAdrPar[1]

    clientMsg = "Message from Client:{}".format(operacao)
    clientIP  = "Client IP Address:{}".format(adr)
    response = atividadeTS(operacao,nome,topico,mensagem)
    
    if type(response) is list:
    	response_aux = "Mensagens encontradas no topico " + topico + ":\n"
    	i = 0
    	while i < len(response):
    		response_aux = response_aux + response[i]['mensagem'] + "\n"
    		i +=1
    else:
    	response_aux = response

    socketservidor.sendto(str.encode(response_aux), adr)