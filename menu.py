

import adivinhacao
import forca

def seletor():
    print("************************************")
    print("*******Selecione o seu jogo!********")
    print("************************************")

    print("Escolha seu jogo: \n (1)Jogo da adivinhação   (2)Jogo da forca \n")

    jogo = int(input("-> "))

    if (jogo == 1):
        print ("jogando o jogo da adivinhação.")
        adivinhacao.jogar()
    elif (jogo==2):
        print ("jogado o jogo da forca.\n")
        forca.jogar()
