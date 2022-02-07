from virp5up import VIPR

ln=[0,0,0,0]
def mainmenu():
    print("""
             Bem vindo(a) a Calculadora eletrica.
             
             Escolha o caluclo que deseja realizar:
             1- Tensao,Potencia,Corrente, Resistencia
             2- Lei de Ohm, Serie/Paralelo
             3-????
          """)
    
def continuar():
        y=input("""
                 Digite s para continuar 
                ou qualquer tecla para sair: 
                """)
        if (y=="s") or (y=="S"):
            print(" Voce desejou continuar.\n")
            opcmenu()
        else:
            print(" Ate  a proxima")
            exit()
            
def opcmenu():
    mainmenu()
    
    opc=0
    while opc>=0 and opc<4:
        if opc==0:#escolhe a opção
            print("\n Digite a opção desejada:")
            try:
              
                x=int(input())
                if x>0 and x<4:
                    opc=x
                     
                else:
                    print(" \nOpção não encontrada.\n")
            except:
                print(" \nOpção invalida.\n")
                
        if opc==1:#chama o arquivo virp e faz os calculos dele
            print("\n\n")
            VIPR()
            continuar()
            
        if opc==2:
            print("Aqui vai algo 2")
            break
        if opc==3:
            print("Aqui vai algo 3")  
            break  
            

opcmenu()