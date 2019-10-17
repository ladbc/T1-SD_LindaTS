#devemos utilizar semáforos pra fazer bloqueante??
#criar um servidor http é fazer linda space com wrapper rest??

import http.server
import socketserver
import os
import sys
import socket

defPort = 8080

#Definição do formato da entrada do micro-blog
class Entrada(object):
	"""docstring for Entrada"""
	def __init__(self, topico, menssagem):
		super(Entrada, self).__init__()
		self.topico = arg
		self.menssagem = 


#Definição do servidor do micro-blog
class Servidor(object):
	"""docstring for Servidor"""
	def __init__(self, PORT = defPort):
		super(Servidor, self).__init__()
		self.arg = arg

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)
		
	def atividade(comando):		#Definição do recebimento de atividade no servidor pelo cliente???
			if comando == 'out':
						
			if comando == 'in' :

			if comando == 'rd' :
				
			else:
				return False

#Definição do cliente do micro-blog		
class Cliente(object):
	"""docstring for Cliente"""
	def __init__(self, PORT, SOCKET):
		super(Cliente, self).__init__()
		self.arg = arg
		
	def out_tuple(comando, topico, menssagem):		#Operação de inserção no tuple space
	#Postagem de conteúdo por tópicos
		

	def in_tuple(comando, topico, menssagem):			#Operação de retirada no tuple space BLOQUEANTE
	#Retirada de conteúdo somente por quem postou
		

	def rd_tuple(comando, topico):			#Operação de cópia do template de tupla no tuple space BLOQUEANTE
	#Obtenção de conteúdo por tópicos 
	