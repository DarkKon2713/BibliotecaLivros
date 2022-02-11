
def menu():
    cont=0
    x=0
    while x==0:
        try:
            x=int(input("Digite o primeiro numero da sequencia:"))
            x1=x+1
            while cont <10:
                xt=x+x1
                print(xt)
                x=x1
                x1=xt
                cont=cont+1
                
        except:
            print("Digite um numero inteiro")
    return x

menu()
