def exponencial(base, expoente):
    resp = i = 1
    if expoente >= 0:
        while i <= expoente:
            resp *= base
            i += 1
        return resp
    else:
        expoente = expoente * -1
        while i <= expoente:
            resp *= ((1 / base))
            i += 1
        return resp


base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
print(f'O resultado de {base}^{expoente} = {exponencial(base, expoente)}')

