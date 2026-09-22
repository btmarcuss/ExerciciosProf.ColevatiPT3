#Declarção de variáveis
valor1: float = 0.0
valor2: float = 0.0

def maiorentre():
    if (valor1 - valor2) > 0:
        print (f"O maior valor é: {valor1}")
    elif (valor1 - valor2) < 0:
        print (f"O maior valor é: {valor2}")
    else:
        print("os valores são iguais.")

def main():
    global valor1
    global valor2
    valor1 = float(input("Digite o primeiro valor:"))
    valor2 = float(input("Digite o segundo valor:"))
    maiorentre()

if (__name__ == '__main__'):
    main()