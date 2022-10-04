#Escreva uma função que, que recebe uma nota que representa a nota de um estudante entre 
# 0 e 5, converte o valor de nota para um americano mostrado abaixo.
#A = 5
#A− = 4,77
#B + = 4,33
#B = 3,9
#B− = 3,47
#C + = 3,0
#C = 2,6
#C− = 2,17
#D = 1,3
#F = 0,0
from ast import Break

n=float(input('NOTA PARA ANALISE ATÉ 5:\n'))
while n <= 5:
    if n >= 4.78:
        print("A")
        break
    if n >= 4.77:
        print("A-")
        break
    if n >= 4.33:
        print("B+")
        break
    if n >= 3.9:
        print("B")
        break
    if n >= 3.47:
        print("B-")
        break
    if n >= 3.0:
        print("C+ ainda está no meio do caminho")
        break
    if n >= 2.6:
        print("C você ainda tem muito que aprender")
        break
    if n >= 2.17:
        print("C- falta estudar")
        break
    if n >= 1.3:
        print("D perdeu o note")
        break
    if n >= 0:
        print("F perdeu o note")
        break