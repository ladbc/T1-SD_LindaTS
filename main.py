from LindaTupleSpace import Client

def main():
  c = Client(('', 5050))
  option = input("menu \n 1 - out \n 2 - in \n 3 - rd \n")
  if option == '1':
    print("Você escolheu enviar uma mensagem! \n Escreva as entradas \n")
    topico = input("Tópico: ")
    mensagem = input("Mensagem: ")
    c.out_tuple(topico, mensagem)
  elif option == '2':
    print("Você escolheu apagar uma mensagem! \n Escreva as entradas \n")
    topico = input("Tópico: ")
    mensagem = input("Mensagem: ")
    c.in_tuple(topico, mensagem)
  elif option == '3':
    print("Você escolheu enviar uma mensagem! \n Escreva as entradas \n")
    topico = input("Tópico: ")
    c.rd_tuple(topico)

if __name__ == '__main__':
  main()