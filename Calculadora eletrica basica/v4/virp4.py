l = [0, 0, 0, 0]

# l[0]=tensao
# l[1]=corrente
# l[2]=potencia
# l[3]=resistencia


def calculadora():
    
    if l[0] and l[1] > 0:  # tensao, corrente
        l[2] = (l[0]*l[1])
        l[3] = (l[0]/l[1])
        return

    if l[0] and l[2] > 0:  # tensao, potencia
        l[1] = (l[2]/l[0])
        l[3] = (l[0]/l[1])
        return

    if l[0] and l[3] > 0:  # tensao,resistencia
        l[1] = (l[0]/l[3])
        l[2] = (l[0]*l[1])
        return

    if l[1] and l[2] > 0:  # corrente,potencia
        l[0] = (l[2]/l[1])
        l[3] = (l[0]/l[1])
        return

    if l[1] and l[3] > 0:  # corente,resistencia
        l[0] = (l[1]*l[3])
        l[2] = (l[0]*l[1])
        return

    if l[2] and l[3] > 0:  # potencia,resistencia
        l[0] = ((l[2]*l[3])/(l[2]*l[3]))
        l[1] = (l[2]/l[0])
        return
    else:
        print("\nVocê não tem dados suficientes.\n")
    return


def menu():
      print("""
              Digite o simbolo da variavel que voce tem:
              P-Potencia
              V-Tensao
              I-Corrente
              R-Resistencia
            """)


def opcao():
      contador = 0
      while contador < 2:
            menu()
            opc = input()
            
            if (opc == "V" or opc == "v"):
                 try:
                     v = int(input("\nDigite o valor da Tensão:"))
                     l[0] = v
                     contador = contador+1
                 except:
                   print("\nError\n")   
            if (opc =="I" or opc=="i"):
                  try:
                    i= int(input("\nDigite o valor da Corrente: "))
                    l[1]=i
                    contador=contador+1
                  except:
                    print("\nError\n")
            if (opc=="P" or opc=="p"):
                  try:
                    p=int(input("\nDigite o valor da Potencia:"))
                    l[2]=p
                    contador=contador+1
                  except:  
                    print("\nError\n")
            if (opc=="R" or opc=="r"):
                  try:
                    r=int(input("\nDigite o valor da Resistencia: "))
                    l[3]=r
                    contador=contador+1
                  except:
                    print("\nError\n")
            else:
              print("\nDigite uma opçao valida.\n")           
      return l
    
print(" Bem vindo a Calculadora Eletrica.\n")
opcao()
print(l)
calculadora()
print(l)
print(f""" 
          Tensao:{l[0]}
          Corrente:{l[1]}
          Potencia:{l[2]}
          Resistencia:{l[3]}
           
          """)
