
def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ", x+y)


def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ", x-y)


def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ", x*y)


def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ", x/y)


opcao = 1


def menu():
    
    opcao=6
    while opcao==6:
        print("0. Sair")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicação")
        print("4. Divisão ")

        try:
            valor = int(input("Opção: "))
            if (valor>=0) and (valor<=4):
                opcao=valor
            
            if (opcao==0):
                break

            if(opcao == 1):
                soma()
            if(opcao == 2):
                subtracao()
            if(opcao == 3):
                multiplicacao()
            if(opcao == 4):
                divisao()
        except:
            print("Digite um valor valido")

menu()
