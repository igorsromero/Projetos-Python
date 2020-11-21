def somatoria(valores, i):
    if i == (len(valores)-1):
        return valores[i]
    else:
        return valores[i] + somatoria(valores, i+1)


def somatoriato(valor1, valor2):
    vetor = [int(each) for each in range(valor1, valor2)]
    return somatoria(vetor, 0)
