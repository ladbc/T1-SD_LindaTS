# T1-SD_LindaTS
Trabalho 1 de Sistemas Distribuídos - Linda Tupple Space

Parte1: desenvolva um sistema em python que implemente uma espaço de dados compartilhado persistente, nos moldes do Linda Tuplespace (com as operações in, rd e out) que permita a implementação de um mini-blog com postagens de conteúdos por tópicos, sua leitura por tópicos e a retirada da mensagem somente por quem postou.

Parte 2: escreva um wrapper usando REST api neste sistema que permita a conexão de clientes remotos a este microblog se conectarem  através de REST. 

Requisitos da aplicação: Python 3.7

Para testar a aplicação:
	1- Abra dois terminais, rode primeiro o arquivo servidor.py em um deles e o arquivo LindaTupleSpace.py em outro
	2- A partir das indicações realize ações no Tupple Space
	3- Observe as mensagens de resposta tanto no arquivo LindaTupleSpace.py quanto servidor.py