import iterativo
import recursivo

while True:
    try:
        opt = input("De qual forma deseja calcular?\n[1]Iterativo\n[2]Recursivo\n[3]Recursivo entre números")
        opt = int(opt)
        if opt == 1:
            vetor = [int(each) for each in input("Insira os valores separados por espaço\n").split()]
            print(iterativo.somatoria(vetor))
            break
        elif opt == 2:
            vetor = [int(each) for each in input("Insira os valores separados por espaço\n").split()]
            print(recursivo.somatoria(vetor, 0))
            break
        else:
            vetor = [int(each) for each in input("Insira dois valores separados por espaço.\n").split()]
            print(recursivo.somatoriato(vetor[0], vetor[1]))
            break
    except ValueError:
        print("Opção inválida.\n")
