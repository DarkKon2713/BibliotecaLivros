import random
l=[0,0,0]
resposta=0
tentativas=1
def inicial():
    
    print(" Bem vindo ao jogo de adivihação\n")
    while l[0] <1:
        try:
            l[0]=int(input("Digite o inicio do intervalo entre os numeros:"))
            while l[1]==0:
                try:
                    l[1]=int(input("Digite o numero final do intervalo entre os numeros:"))
                    
                except:
                    print("Digite um numero inteiro")
                    
        except:
            print("Digite um numero inteiro")
    return l

inicial()

if l[0]> l[1]:
    l[2]=random.randint(l[1],l[0])
    ini=l[1]
    fim=l[0]
  
    
if l[1]> l[0]:
    l[2]=random.randint(l[0],l[1])
    ini=l[0]
    fim=l[1]
    
    
while resposta != l[2]:
    try: 
        resposta=int(input("Digite o numero que vc acha que é:"))
        if  resposta > fim:
            print(" Seu numero é superior ao numero inicial")
        if resposta < ini:
            print(" Seu numero é menor ao numero final ")
        if (resposta>=ini) and (resposta<=fim):
            if resposta == l[2]:
                print(f" Voce acertou.\n Em {tentativas} tentativas.")
            if resposta !=l[2]:
                print(" Resposta errada")
                tentativas=tentativas+1
                print(f"errou num {tentativas}")
                if resposta> l[2]:
                    print("Voce adivinhou muito alto")
                if resposta< l[2]:
                    print("Voce adivinhou muito baixo")
                
    except:
        print("Digite um numero inteiro")
    