import string


def criptografar(frase):
    try:
        for i in range(26):
            for j in range(26):
                if frase[i].upper() == alfabeto[j]:
                    if j+3 > 25:
                        j = j-23
                        newfrase.append(alfabeto[j])
                    else:
                        newfrase.append(alfabeto[j+3])
    except IndexError:
        pass
    print(''.join(newfrase))


def descriptografar(frase):
    try:
        for i in range(26):
            for j in range(26):
                if frase[i].upper() == alfabeto[j]:
                    if j-3 < 0:
                        j = j+23
                        newfrase.append(alfabeto[j])
                    else:
                        newfrase.append(alfabeto[j-3])
    except IndexError:
        pass
    print(''.join(newfrase))


alfabeto = list(string.ascii_uppercase)
frase = input('Insira uma frase: ')
newfrase = []
while True:
    try:
        opt = int(input('Escolha a opção:\n[1] Criptografar\n[2] Descriptografar\n'))
        if opt == 1:
            criptografar(frase)
            break
        elif opt == 2:
            descriptografar(frase)
            break
    except ValueError:
        print('Coloque um valor válido.\n')
        continue
