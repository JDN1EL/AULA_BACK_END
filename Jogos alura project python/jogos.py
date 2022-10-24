def games():
    import forca
    import advinhação
    print ('','*'*26,"\n{}{}Escolha seu jogo!{}\n".format(' ','*'*4,'*'*5),'*'*26,"\n(1) Forca (2) Advinhação")#___só pra exercitar
    jogo = int(input('Qual o jogo ?\n'))
    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print ("Jogando adivinhação")
        advinhação.jogar()

if (__name__=="__main__"):#____1 if e os nomes tem duas underscore ou sublinhados em pt - br
    games()