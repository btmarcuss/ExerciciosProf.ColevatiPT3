#Declaração de Variáveis
valor1: float = 0.0

def divisivel3e2():
    if (valor1 %2) == 0 and (valor1 %3) == 0:
        print ("O valor é divisível por 2 e por 3.")
    elif (valor1 %2) == 0 and (valor1 %3) > 0:
        print ("O valor é divisível apenas por 2.")
    elif (valor1 %3) == 0 and (valor1 %2) > 0:
        print ("O valor é divisível apenas por 3.")
    else:
        print ("O valor NÃO é divisível nem por 2 nem 3.")

def main():
    global valor1
    valor1 = int(input("Digite o primeiro valor:"))
    divisivel3e2()

if (__name__ == '__main__'):
    main()