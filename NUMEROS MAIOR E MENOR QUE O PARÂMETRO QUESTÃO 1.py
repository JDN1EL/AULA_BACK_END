# 01 - Escreva uma função que receba um número como parâmetro, para cada número menor que o parâmetro:
 
#• a função imprime "Back" para número múltiplo de três
#• a função imprime "Front" se o número for múltiplo de cinco
#• e imprime "Back e Front" se o número for múltiplo de três e cinco.
#32 • caso o número não seja múltiplo nem de três nem de cinco imprima o numero

a = int (input ('digite um número para verificação:\n'))
def mult (mt):
    if mt %3 == 0 :
        print ("Back")
    if mt %5 == 0 :
        print ("Front")

mult(a)

#def mult2 (bf):
    #if bf ("Back") and ("front") == 0:
        #print('Back e Front')

#mult2(a)




#def soma(mt):
    #if mt%3 == 0:
        #print("back")

#p = int (input ('escreva um numero:\n'))
#soma(p)