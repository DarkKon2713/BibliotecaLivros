produto1=[]
produto2=[]
operador=[]
resultados=[]
masters=[]

def inicio():
    errorcont=0
    x=input(" Enter problems separte by comma: ")
    y=x.split(",")
    for i in y:
       #positivo
        
        if "+" in i:
            z=i.split("+")
            z1=int(len(z[0]))
            #print(z1)
            z2=int(len(z[1]))
            #print(z2)
            if ((z1 <=4) and (z2<=4)):
                   
                v1=int(z[0])
                v2=int(z[1])
                resultado= v1+v2
                produto1.append([v1])
                produto2.append([v2])
                operador.append(["+"])
                resultados.append([resultado])
                
                
                #print("Conta positiva")
                #print(resultado)
                
            if ((z1>=5) or (z2>=5)):
                print(len(z[0]))
                print(len(z[1]))
                print("Error: Numbers cannot be more than four digits.")   
                errorcont=errorcont+1
  
        ## negativo      
        if "-" in i:
            z=i.split("-")
            z1=int(len(z[0]))
            #print(z1)
            z2=int(len(z[1]))
            #print(z2)
           
            if ((z1 <=4) and (z2<=4)):
                   
                v1=int(z[0])
                v2=int(z[1])
                resultado= v1-v2
                produto1.append([v1])
                produto2.append([v2])
                operador.append(["-"])
                resultados.append([resultado])
                
                #print("Conta negativa")
                #print(resultado)
                
            if ((z1>=5) or (z2>=5)):
                print(len(z[0]))
                print(len(z[1]))
                print("Error: Numbers cannot be more than four digits.")
                errorcont=errorcont+1 
            
                
            
        
        if ("-" not in i )and ("+" not in i):
            print("Error: Operator must be '+' or '-'.")
            errorcont=errorcont+1
        
        if errorcont==5:
                print("Error: Too many problems.")
                break
        
    return produto1,produto2,operador,resultados


def prints():
    #print(f"{produto1:,2.f}")  
    #print(produto2)
    #print(operador)
    #print(resultados)    
    #return
    n=len(produto1)
    for m in range(0,n):
        print(f" {produto1[m]}\n{operador[m]}{produto2[m]}\n-----\n {resultados[m]}")

inicio()
prints()
