import random
numero = int(random.randrange(0, 11))
while True:
    try:
        chute = int(input('Chute um valor entre 0 e 10: '))
        if chute == numero:
            print('Parabéns!! Você acertou!!\n')
            break
        elif chute > numero:
            print('Você chutou alto\n')
        else:
            print('Você chutou baixo\n')
    except ValueError:
        print('Digite um valor válido.\n')
