def verificarAnagrama(palavra1, palavra2):
    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False



palavra1 = (str(input('Digite a 1º palavra: '))).lower().strip()
palavra2 = (str(input('Digite a 2º palavra: '))).lower().strip()
print(verificarAnagrama(palavra1, palavra2))



