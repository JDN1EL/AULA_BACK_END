from tkinter.tix import Tree


lista = []#Vamos chamar isso de jeitinho brasileiro ou pros intimos "gambiarra!"
def dados (numero):
    numero = int (input ('Número para parâmetro verificação :\n'))
    lista = int (input ('Digite seus números: \n'))
    while numero == lista:
        print ([numero]+[lista],"True\n")
    else:
        print ("False\n","Número não encontado")


#Escreva uma função que recebe como entrada uma lista de números e retorna
#True se um número passado como parâmetro está 
#presente na lista.

#def mult(x, num=2):
    #return x, x*num
#a,b = mult(2)

#print (a,b)
#a,b=mult(2, num=10)

#print(a,b)
#a,b=mult(3,5)
#print(a,b)

#return x == ("True")#Infelizmente um True falso, porquê ele já tá sendo usado pra outra coisa:')







#while ln != "":
    #lista = int(input('Uma lista de números: '))
    #ln.append (lista)
    #print(ln)



    #if lista > ln:
        #print ([lista],"False")
    #else:
        #print ([lista],"False")