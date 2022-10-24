import random
print('','*'*31,"\n{}{}Bem vindo ao Jankenpô{}\n".format(' ','*'*5,'*'*5),'*'*31)
while True:
    jogador_escolhe = int(input('(1) Para pedra (2) Para papel (3) Para tesoura\n'))
    bot = random.randrange (4,7)#4 = pedra, 5 = papel, 6 = tesoura
    textos_resposta = random.randrange (8,11)
    from time import sleep
    sleep(1)
    print('Pedra')
    sleep(1)
    print('Papel')
    sleep(1)
    print('Tesoura!\n')#PARTE DA CONTAGEM

    if (jogador_escolhe == 1):
        print ('Você escolheu -----> pedra')
    if (jogador_escolhe == 2):
        print ('Você escolheu -----> papel')
    if (jogador_escolhe == 3):
        print ('Você escolheu -----> tesoura')#PARTE DA ESCOLHA DO JOGADOR

    if (bot == 4):
        print ('Eu escolhi --------> pedra')
    if (bot == 5):
        print ('Eu escolhi --------> papel')
    if (bot == 6):
        print ('Eu escolhi --------> tesoura')#PARTE DA ESCOLHA DO BOT


    if ((bot == 4 and jogador_escolhe == 1) or (bot == 5 and jogador_escolhe == 2) or (bot == 6 and jogador_escolhe == 3)):
        if (textos_resposta == 8):
            print('\nDeu empate')
        if (textos_resposta == 9):
            print('\nEmpatamos nessa')
        if (textos_resposta == 10):
            print('\nGêmeos, ninguém ganhou\nVamos mais uma pra decidir!')
        
    if ((bot == 4 and jogador_escolhe == 3) or (bot == 5 and jogador_escolhe == 1) or (bot == 6 and jogador_escolhe == 2)):
        if (textos_resposta == 8):
            print('\nVocê perdeu')
        if (textos_resposta == 9):
            print('\nGanhei! haha!')
        if (textos_resposta == 10):
            print('\nEu sou o melhor!, venci \nque tal mais uma patinho\n')

    if ((bot == 4 and jogador_escolhe == 2) or (bot == 5 and jogador_escolhe == 3) or (bot == 6 and jogador_escolhe == 1)):
        if (textos_resposta == 8):
            print('\nVocê ganhou')
        if (textos_resposta == 9):
            print('\nVenceu, melhor de três que tal!')
        if (textos_resposta == 10):
            print('\nDROGA!, vamos denovo!')#PARTE DA INTERAÇÃO DO BOT E JOGADOR
    
    denovo=int(input('\n(1) para jogar denovo ou qualquer tecla para sair\n'))
    if (denovo != 1):
        break




