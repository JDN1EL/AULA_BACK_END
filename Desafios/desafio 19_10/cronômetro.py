from time import gmtime, strftime, sleep, time, time_ns
from wsgiref.handlers import format_date_time
import os
interação = int(input('Digite o número para cronometragem\nOU\nDigite 0 para contagem infinita:\n'))
interação = (interação * 60)#uma simples multiplicação
numeros = 0
if interação >= 0:
    numeros + interação
while int:
    sleep(0.6)#encontrando o valor adequado para esleep pode aperfeiçoar o crônometro como com (0.06) por exemplo
    numeros += 1
    print(format_date_time(numeros)[18:-3:])
    if numeros == interação:
        print('ACABOU\n  O\n  TEMPO!')
        break
