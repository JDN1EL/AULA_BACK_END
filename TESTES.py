"""pj cash -  banco - com snake case
No banco dele ele quer ter 1 arquivo 

cliente.py
o arquivo recebe o cadastro dos clientes


conta corrente.py
numero cliente
número da conta corrente
saldo

minhas transferencias.py
informações das transferencias que a conta for fazendo

meus imprestimos.py
numero conta
numero cliente
valor emporestimo 
data emprestimo


meusdepositos.py
numero cliemnte
numero conta conta
valor

meus saques.py
numero da cliente 
numero da conta
valor sacado

pj transações.py
funções referentes ao banco
nota: funções que vão fazer o que há nos outros 

identificação de arquivos"""
#import random
#n = 1
#a = 9
#lista = [a*random.random() for n in range(n)]
#print(lista)#                       ______
    #                                    |__________range cria uma sequencia de numeros 
#                                                

cc = ""
if cc == "":
        print('Esse é o seu número de cliente\nLembrese de anotar e guardá-lo')
        import random
        total_de_listas = 1
        caractere_extra = 9
        numero_cliente = [caractere_extra*random.random() for total_de_listas in range(total_de_listas)]
        print (numero_cliente[::-1])
        nca = {'ncarmazenado':numero_cliente}
        print (nca ['ncarmazenado'])