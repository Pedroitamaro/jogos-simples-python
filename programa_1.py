print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("digite o seu número: ")

chute = int(chute_str)

acertou = chute == numero_secreto

maior = chute>numero_secreto

menor = chute<numero_secreto

if (acertou):
    print("Você acertou!")

else:
    if (maior):
        print("Você errou! Seu chute foi um valor mais alto que o número secreto.")
    elif (menor):
        print("Você errou! Seu chute foi um valor mais baixo que o número secreto.")

print("fim de jogo.")

