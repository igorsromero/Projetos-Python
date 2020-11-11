from random import randrange
while True:
    jogarDado = input("Você gostaria de jogar o dado?\n")
    if jogarDado == "Sim":
        print('O valor tirado foi: {} \n'.format(randrange(1, 7)))
    elif jogarDado == "Não":
        break
    else:
        print("Resposta Inválida\n")
