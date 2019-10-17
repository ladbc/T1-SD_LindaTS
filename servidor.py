#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import http.server
import socketserver
import os
import sys
import socket
import json
from main import unpack

porta   = 8080
bufferSize  = 1024
msgFromServer = "Cliente conectado ao servidor"
bytesToSend = str.encode(msgFromServer)
tuple_space = []

#Definicao da atividade a ser realizada do cliente pelo servidor
def atividadeTS(comando,nome,topico,mensagem):
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

# Cria o socket para comunicacao
socketservidor = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
socketservidor.bind(('', porta))		# Une o cliente ao socket servidor

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