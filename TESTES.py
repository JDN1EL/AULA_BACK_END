#def t(txt):
    #print('_'*22)
    #print(txt)
    #print('_'*22)

#t('daniel\n'[::-1])

equ = ("Equilátero")
esc = ("Escaleno")
iso = ("Isósceles")
v1 = int(input('Valor 1\n'))#___________v1, v2, v3 são os valores digitados, int é inteiro.
v2 = int(input('Valor 2\n'))#____|
v3 = int(input('Valor 3\n'))#_|
if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:#Perceba a linha caindo lá no ultimo else, foi a forma que achei de pular conflitos
    if v1 == 0 or v2 == 0 or v3 == 0:
        print('Valor impossível.\nSe um lado tem 0 não é um triângulo kkkkkk')#Sobra das minhas falhas, mas deixei ai, se passar na verificação de cima cai aqui:)
    else:
        if v1 == v2 and v1 == v3 and v3 == v2:
            print(equ)
        elif v1 == v2 != v3 or v1 == v3 != v2 or v2 == v3 != v1:#"O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa."
            print(iso)
        else:
            print(esc)
else:   
    print('''Valor impossível\nSe a soma entre os dois não for maior que terceiro, esse triângulo não é triangulo, ex:.
  10cm
    |___________
    \\          /------>3cm
     \\--------------->4cm''')
