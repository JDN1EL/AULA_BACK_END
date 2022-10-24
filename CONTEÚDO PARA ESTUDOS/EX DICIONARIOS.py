from random import randrange
import random
tabela = {
    1:'bom dia',
    #_____   #______
       #|________|__________________________MANHÃ GANHA O BOM DIA COMO REGISTRO
    2:'boa tarde',
    3:'boa noite'}
p = random.randrange(1,4)
print(tabela[p])
#|______________________|_____________________FAZ ASSIM QUANDO CHAMA ALGUÉM DO DICIONÁRIO
