

#variaveis

def menu():#menu de virp
      print("""
              Digite o simbolo da variavel que voce tem:
              
              
            """)
def pedivalor():
    pedir=0
    while pedir==0:
        try:
            valorpedido=float(input("\nDigite o valor da resistencia:"))
            if valorpedido>0:
                pedir=1
        except:
            print("\nDigite um valor valido:")
    return valorpedido
    
    
         
pedivalor()

    
    