print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************\n")

numero_secreto = 42

tentativas_str = (input ("\nEm quantas tentativas você quer tentar acertar: "))
tentativas = int (tentativas_str)

while (tentativas > 0):
    
    if (tentativas>0):
        print ("Você tem", tentativas, "tentativas restantes")
    

    chute_str = input ("\ndigite o seu número: ")

    chute = int (chute_str)
    acertou = chute == numero_secreto
    
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print ("Você acertou!\n")
        print ("Fim de jogo!\n")
    else:
        if (maior):
            tentativas -= 1
            print ("\nVocê errou! Seu chute foi um valor mais alto que o número secreto.\n")
        elif (menor):
            tentativas -= 1
            print ("Você errou! Seu chute foi um valor mais baixo que o número secreto.\n")

if (tentativas == 0):
    print ("Suas tentativas acabaram.\n")
    print ("Fim de jogo!\n")

