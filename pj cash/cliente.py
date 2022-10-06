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

uidentificação de arquivos"""

sim = 1
não = 2
dados = int(input('Bom dia\n quer fazer um cadastro?\n1 para SIM\n    OU \n2 para NÃO\n'))
if dados == 1:
    dados_confirmados = {'nome':input('Seu nome: '),
    'numero':int(input('Seu número: ')),
    'email':input('Seu E-mail: '),
    'CPF':int(input('Seu CPF: '))}













#"""enterr = 1
#inicioum = input ('Olá, quer iniciar\n1 para iniciar\nOu qualquer outra para sair:\n')
# inicioum == enterr:
#armazenamento = {'cliente':int(input('Numero do cliente:\n')),
#        'numero':int(input('Numero da conta:\n')),
#        'emp':int(input('Valor do seu emprestimo:\n'))
#    })
#    break"""
#if armazenamento == armazenamento:
    #print(armazenamento ['cliente'],armazenamento ['numero'], armazenamento ['emp'])