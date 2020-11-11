from random import randrange


def contadordelinhas():
    arquivo1 = open('respostas.txt', 'r', encoding='utf8')
    tamanho = len(arquivo1.readlines())
    arquivo1.close()
    return tamanho


while True:
    quantidadeLinhas = contadordelinhas()
    try:
        arquivo = open('respostas.txt', 'r', encoding='utf8')
    except FileNotFoundError:
        print('O banco de respostas está indisponível.\n')
        break
    input('O que você gostaria de perguntar se deve ou não fazer?\n')
    print('Quantidade de linhas: ', quantidadeLinhas)
    num = randrange(0, quantidadeLinhas)
    linhas = arquivo.readlines()
    print(linhas[num] + '\n')
    arquivo.close()
    goOn = input('Gostaria de fazer mais alguma pergunta?\n')
    if goOn == 'Não':
        break
    else:
        continue
