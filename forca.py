def jogar():
    print("************************************")
    print("*****Bem vindo ao jogo da Forca*****")
    print("************************************")

    palavra_secreta = "PYTHON"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute.isupper
        index = 1
        for letra in palavra_secreta:
            if(chute==letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index += index
    print("Fim de Jogo")

if(__name__== "__main__"):
    jogar()