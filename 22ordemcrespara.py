#Declaração de Variáveis
valor1: int = 0
valor2: int = 0

def ordemcresc():
    if ((valor1 - valor2) > 0):
        print (valor2)
        print (valor1)
    elif ((valor1 - valor2) == 0):
        print (valor1)
        print (valor2)
    else:
        print (valor1)
        print (valor2)

def main():
    global valor1
    global valor2
    valor1 = int(input("Digite o primeiro valor:"))
    valor2 = int(input("Digite o segundo valor:"))
    ordemcresc()

if (__name__ == '__main__'):
    main()