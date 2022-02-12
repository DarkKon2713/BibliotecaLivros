import sys


l=[[1,2,3],[4,5,6],[7,8,9]]

opcao=0
def menu():
    print("Bem vindo ao jogo da velha.\n Player 1 X e Player 2 O")

def jogando():
    player=0
    fim=0
    

    while fim==0:
        print(f"{l[0][0] }  {l[0][1]}  {l[0][2]} \n--------\n{l[1][0]}  {l[1][1]}  {l[1][2]} \n--------\n{l[2][0]}  {l[2][1]}  {l[2][2]}")
        play=player%2
        ganhador(play)
        
        try:
            
            if play==0:
                player1(local())
                player=player+1           
            if play==1:
                player2(local())
                
                player=player+1
        except:
            print("não deu")

def player1(opcao):
    for i in range(3):
        for j in range(3):
            if(l[i][j]==opcao):
                #print("achei")
                l[i][j]="X"
                
                       
        
def player2(opcao):
    
    for i in range(3):
        for j in range(3):    
            if l[i][j]==opcao:
                #print("achei")
                l[i][j]="O"
            

def ganhador(play):
    for i in range(3):
        if ((l[i][0]) ==(l[i][1])) and((l[i][1])== (l[i][2])):
            print("ganhou linha")
            if play==0:
                print(f" O ganhador foi Jogador 2") 
            if play==1:
                print(f" O ganhador foi Jogador 1")
            exit()

        if ((l[0][i]) ==(l[1][i])) and((l[1][i])== (l[2][i])):
            print("ganhou Coluna")
            if play==0:
                print(f" O ganhador foi Jogador 2") 
            if play==1:
                print(f" O ganhador foi Jogador 1")
            exit()
            
        if (((l[0][0]) ==(l[1][1])) and((l[1][1])== (l[2][2])) or (((l[0][2]) ==(l[1][1])) and((l[1][1])== (l[2][0])))):
            print("ganhou em x")
            if play==0:
                print(f" O ganhador foi Jogador 2") 
            if play==1:
                print(f" O ganhador foi Jogador 1")
            exit()
        if (l[0][0]!=1 and l[0][1]!=2 and l[0][2]!=3 and
        l[1][0]!=4 and l[1][1]!=5 and l[1][2]!=6 and
        l[2][0]!=7 and l[2][1]!=8 and l[2][2]!=9):
            print("Ninguem ganhou ")
            exit()
                    

def local():
    opcao=0
    while opcao==0:
        continuar=0
        
        try:
            while continuar==0:
                    opc=int(input("Digite o numero  do local:"))
                    if opc in range(1,10):
                        for espec in range(3):
                            if opc in l[espec]:
                                opcao=opc
                                continuar=1
                                return opcao

        except:
            print("Opcao invalida")

jogando()
