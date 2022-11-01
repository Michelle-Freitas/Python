def fibonacci(termo):
     ultimo = penultimo = 1
     if (termo == 0) or (termo == 1):
          return ultimo
     else:
          i=2
          while i <= termo:
               fn = ultimo + penultimo
               penultimo = ultimo
               ultimo = fn
               i += 1
          return fn


num = int(input('Digite a posição que gostaria [inicio é 0]: '))
print(f'O resultado da posição {num} é: {fibonacci(num)}')

