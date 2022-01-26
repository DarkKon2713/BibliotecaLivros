#terceira tentativa

v = 0 #tensao
i = 0 #corrente
r = 0 #resistencia
p = 0 #potencia
contador=0

def menu():
    print("""
           
           Digite o simbolo das variaveis que você tem:
           P-Potencia
           V-Tensão
           I-Corrente
           R-Resistência
          """)
    
    return
   
while contador<2 :
    menu()
    opcao=input()
    if ((opcao=="V") or (opcao=="v")) and v==0 :    
        try:
            v=float(input("Digite a Tensão: ")) 
            contador = contador+1
        except:
            print("Error")
        
    elif ((opcao=="P") or (opcao=="p")) and p==0 : 
        try:  
            p=float(input("Digite a Potencia: ")) 
            contador = contador+1
        except:
            print("Error")
            
    elif ((opcao=="I") or (opcao=="i")) and i==0:
        try:
            i=float(input("Digite a Corrente: ") ) 
            contador = contador+1
        except:
            print("Error")
            
    elif ((opcao=="R") or (opcao=="r")) and r==0:  
        try:
            r=float(input("Digite a resistencia: "))
            contador = contador+1
        except:
            print("Error")
        
    else:
        print ("Digite uma opçao valida\n")
  
    if r and i > 0:
        v = (r*i)
        p = (r*(i*i))
    if r and v > 0:
        p = (v*v)/r
        i = v/r
    if r and p > 0:
        v = (r*p)/(r*p)
        i = p/r
    if p and v > 0:
        i = p/v
        r = v/i
    if p and i > 0:
        v = p/i
        r = v/i
    if i and v > 0:
        p=v*i
        r=v/i
           

print("\nOs resultados obtidos foram:")
print(f"Tensão:{v}Volts\nCorrente:{i}Amperes\nResistência:{r}Ohms\nPotência:{p}Watts\n")
        
