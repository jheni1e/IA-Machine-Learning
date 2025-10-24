import random
numeroAleatorio = random.randint(1,10)
tentativas = 0
while True:
    num = int(input("Escolha um numero"))
    tentativas =+ 1 
    if numeroAleatorio > num:
        print("O numero aleatorio é menor")

    elif numeroAleatorio < num:
        print("O numero aleatorio é maior")

    elif num + 1  ==  numeroAleatorio or num + 2 ==  numeroAleatorio:
            print("Quase!")

    elif num - 1 ==  numeroAleatorio or num - 2 ==  numeroAleatorio:
            print("Quase!")
print(f"Você acertou o numero era {numeroAleatorio}" )
    
