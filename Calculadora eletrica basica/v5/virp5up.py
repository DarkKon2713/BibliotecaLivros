

#variaveis
l = [0, 0, 0, 0]
r=[]
# l[0]=tensao
# l[1]=corrente
# l[2]=potencia
# l[3]=resistencia
   
def menu():#menu virp
      print("""
              Digite o simbolo da variavel que voce tem:
              P-Potencia
              V-Tensao
              I-Corrente
              R-Resistencia
            """)
   
def calculadora():#calculo de virp
    
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

def cabos():#dimensionamento de cabos
    if (l[1]>0) and(l[1]<=15.5):#cabo 1,5mm
        print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 1,5mm.\n")
        return
    if (l[1]>15.5) and(l[1]<=21):#cabo 2,5mm
        print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 2,5mm.\n")
        return
    if (l[1]>21) and(l[1]<=28):#cabo 4mm
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 4mm.\n")
         return
    if (l[1]>21) and(l[1]<=36):#cabo 6mm 
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 6mm.\n")
         return
    if (l[1]>36) and(l[1]<=50):#cabo 10mm
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 10mm.\n")
         return
    if (l[1]>50) and(l[1]<=66):#cabo 16mm
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 16mm.\n")
         return
    if (l[1]>66) and(l[1]<=89):#cabo 25mm
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 25mm.\n")
         return
    if (l[1]>89) and(l[1]<=111):#cabo 35mm
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 35mm.\n")
         return
    if (l[1]>111) and(l[1]<=134):#cabo 50mm
         print(f"\n Sua corrente é de {l[1]} e o cabo recomendado é 50mm.\n")
         return
    return  
def menu():#menu de virp
      print("""
              Digite o simbolo da variavel que voce tem:
              P-Potencia
              V-Tensao
              I-Corrente
              R-Resistencia
            """)

def opcao():#escolher tensao, corrente e potencia
      l
      contador = 0 
      while contador < 2:
            menu()
            opc = input("Digite a opção desejada:")
            
            if (opc == "V" or opc == "v"):
                while l[0]==0:
                 try:
                     v =float(input("\nDigite o valor da Tensão:"))
                     l[0] = v
                     contador = contador+1
                 except:
                   print("\nError\n")   
            if (opc =="I" or opc=="i"):
                while l[1]==0:
                  try:
                    i= float(input("\nDigite o valor da Corrente: "))
                    l[1]=i
                    contador=contador+1
                  except:
                    print("\nError\n")
            if (opc=="P" or opc=="p"):
                  while l[2]==0:
                    try:
                        p=float(input("\nDigite o valor da Potencia:"))
                        l[2]=p
                        contador=contador+1
                    except:  
                        print("\nDigite um valor valido para Potencia.\n")
            if (opc=="R" or opc=="r"):
                  while l[3]==0:
                      try:
                          r=float(input("\nDigite o valor da Resistencia: "))
                          l[3]=r
                          contador=contador+1
                      except:
                           print("\nDigite um valor valido para Resistencia.\n")
                    
      return l


             
def VIPR():#fazer todas as fuçoes de virp
      
    print(" Calculo de PUI/RUI.\n")
    opcao()
    #print(l)#APAGAR verificar se o dado salvou
    calculadora()
    #print(l)#APAGAR verificar se foi feito os calculos
    print(f""" 
                Tensao:{l[0]}
                Corrente:{l[1]}
                Potencia:{l[2]}
                Resistencia:{l[3]}
            """)
    cabos()
    if l[0] and l[1]>0 and l[2] and l[3]:#reset improvisado
        l[0]=0
        l[1]=0
        l[2]=0
        l[3]=0
     
  
#VIPR()#testar o projeto
