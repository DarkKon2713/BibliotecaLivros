print("Bem vindo a calculadora de eletrica basica. ")
fila = 0
v = 0
i = 0
r = 0
p = 0
contador = 0
concluido=0

while fila<=0:
    
    print("Digite o simbolo das variaveis que você tem:")
    simbol = input(" V-Tensão \n I-Corrente \n R-Resistência \n P-Potência \n")
    if (simbol == "V") or (simbol == "v"):  # Tensao
        while v <= 0:
            try:
                v = float(input("Digite o valor da Tensão: "))
                contador = contador+1
            except:
                print("Digite um numero valido.")
    if (simbol == "I") or (simbol == "i"):  # Corrente
        while i <= 0:
            try:
                i = float(input("Digite o valor da Corrente: "))
                contador = contador+1
            except:
                print("Digite um numero valido.")
    if (simbol == "R") or (simbol == "r"):  # Resistencia
        while r <= 0:
            try:
                r = float(input("Digite o valor da Resitência: "))
                contador = contador+1
            except:
                print("Digite um numero valido.")
    if (simbol == "P") or (simbol == "p"):  # Potencia
        while p <= 0:
            try:
                p = float(input("Digite o valor da Potência: "))
                contador = contador+1
            except:
                print("Digite um numero valido.")
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
    if (simbol != "V") and (simbol != "v") and (simbol != "R") and (simbol != "r") and (simbol != "I") and (simbol != "i")and (simbol != "P") and (simbol != "P"):
        print("Digite uma opção valida.\n")    
    if i>0 and r>0 and v>0 and p>0:
        
      
        print("\nOs resultados obtidos foram:")
        print(f"Tensão:{v}Volts\nCorrente:{i}Amperes\nResistência:{r}Ohms\nPotência:{p}Watts\n")
        fila=int( input("Se deseja fazer outra conta digite 0 \n Para sair digite qualquer outro numero."))    
        
        if fila==0:
            v=0
            p=0
            i=0
            r=0