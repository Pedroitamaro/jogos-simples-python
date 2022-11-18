import random
from random import randrange

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************\n")

numero_secreto = random.randrange(1, 101)

print (numero_secreto)

user_input = (input ("\nEm quantas tentativas você quer tentar acertar: ",))
tentativas = int(user_input)

if(tentativas <= 0):
    print ("Você precisa colocar um número maior que 0.")
    user_input = (input ("\nEm quantas tentativas você quer tentar acertar: ",))
    tentativas =  int(user_input)
    


while (tentativas > 0):
    
    if (tentativas>1):
        
        print ("Você tem", tentativas, "chances.")


    elif (tentativas == 1 and chute != numero_secreto):
        
        print ("Cuidado! Você só tem mais", tentativas, "chance")
    

    chute_str = input ("\ndigite o seu número: ")

    chute = int (chute_str)
    acertou = chute == numero_secreto

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    perdeu = tentativas == 0

    if (acertou):
        tentativas = tentativas + 1
        print ("Você acertou!\n")
        print ("Fim de jogo!\n")
        break

    else:

        if (maior):
            tentativas -= 1
            print ("\nVocê errou! Seu chute foi um valor mais alto que o número secreto.\n")


        elif (menor):
            
            tentativas -= 1
            print ("Você errou! Seu chute foi um valor mais baixo que o número secreto.\n")

perdeu = tentativas == 0

if(perdeu):
    print("Suas chances acabaram. Você perdeu!")
