lista = [ 1, 2, 3, 4, 5, 6 ]

def verificar(lista):
    teste = []
    for i in range(0, len(lista)):
        for j in range (0, len(lista)):
            tentativa = lista[i]*lista[j]
            teste.append(tentativa)

    if 36 in teste:
        return True
    else:
        return False


#print(verificar(lista))

