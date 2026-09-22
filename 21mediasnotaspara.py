#Declaração de variáveis
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4:float = 0.0
media: float = 0.0

def media():
    media = ((n1 + n2 + n3 + n4) / 4)
    if (media < 3.0):
        print ("Retido")
    elif (media > 5.9):
        print ("Aprovado")
    else:
        print ("Exame")

def main():
    global n1
    global n2
    global n3 
    global n4
    n1 = float(input("Digite a nota do Primeiro Bimestre:"))
    n2 = float(input("Digite a nota do Segundo Bimestre:"))
    n3 = float(input("Digite a nota do Terceiro Bimestre:"))
    n4 = float(input("Digite a nota do Quarto Bimestre:"))
    media()

if (__name__ == "__main__"):
    main()