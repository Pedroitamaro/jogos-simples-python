def jogar():
    import random                  #Importando a função random para que possa gerar um número aleatório, é necessário importar esse modulo pois ela não é uma função built in
    from random import randrange


    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1, 101) #gerando o numero aleatório

    user_input = int ( (input ("\nQual nivel de de dificuldade você deseja jogar:\n (1)Fácil  (2)Intermediário  (3)Dificíl  \n-> ",))) #Imput para definir quantas tentativas o jogador terá

    while (user_input>3):
        print("Erro! Por favor selecione um nivel de dificuldade existente")
        user_input = int ( (input ("\nQual nivel de de dificuldade você deseja jogar: (1)Fácil  (2)Intermediário  (3)Dificíl  -> ",)))

    if(user_input==1):
        chances = 15
    elif(user_input==2):
        chances = 10
    elif(user_input==3):
        chances = 5

    tentativas = chances

    while (tentativas > 0): #Esse laço while faz o jogo rodar enquanto o jogador ainda tiver tentativas disponiveis
        
        if (tentativas>1): # Um contador de chances que o jogador ainda tem

            print ("Você tem", tentativas, "chances.")


        elif (tentativas == 1 and chute != numero_secreto): #Alerta que o jogador só tem mais uma chance

            print ("Cuidado! Você só tem mais", tentativas, "chance")


        chute_str = input ("\ndigite o seu número: ") #Input que o jogador colocara a sua resposta

        chute = int (chute_str)
        acertou = chute == numero_secreto

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        perdeu = tentativas == 0

        if (acertou):   #Caso acerto o numero o jogo dirá que acertou e que é fim de jogo
            tentativas = tentativas + 1
            print ("Você acertou!\n")
            print ("Fim de jogo!\n")
            break #Esse comando break serve para que se o jogador ganhe com tentativas de sobra, não imprima quantas chances ele ainda tem

        else:

            if (maior): #Aqui imprime se o chute foi um numero mais alto
                tentativas -= 1
                print ("\nVocê errou! Seu chute foi um valor mais alto que o número secreto.\n")


            elif (menor): #Aqui imprime se o chute foi um numero mais baixo
                
                tentativas -= 1
                print ("Você errou! Seu chute foi um valor mais baixo que o número secreto.\n")

    perdeu = tentativas == 0

    if(perdeu): #Caso o numeor de tentativas zere o programa irá imprimir que o jogador perdeu e que suas chances acabaram
        print("Suas chances acabaram, o numero secreto era:", numero_secreto,".")
        print("Você perdeu!")

if(__name__== "__main__"):
    jogar()
