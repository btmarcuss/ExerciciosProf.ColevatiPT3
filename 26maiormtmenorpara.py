#Declaração de Variáveis
valor1: int = 0
valor2: int = 0

def maiormtmenor():
    if (valor1 > valor2):
        if (valor1 % valor2) == 0:
            print ("O valor maior é multiplo do menor.")
        else:
            print ("O valor maior NÃO é multiplo do menor.")
    elif (valor1 == valor2):
        print ("Os valores são iguais.")
    else:
        if (valor2 % valor1) == 0:
            print ("O valor maior é multiplo do menor")
        else:
            print ("O valor maior NÃO é multiplo do menor.")

def main():
    global valor1
    global valor2
    valor1 = int(input("Digite o primeiro valor:"))
    valor2 = int(input("Digite o segundo valor:"))
    maiormtmenor()

if (__name__ == '__main__'):
    main()