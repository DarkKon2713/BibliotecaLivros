refazer=0
print("Bem vindo a calculadora de eletrica basica. ")
print("Digite os dados soliciatos, se nao tiver digite 0")
while refazer ==0:  
   v = int(input("Digite a tensao: "))
   i = int(input("Digite a corrente: "))
   r = int(input("Digite a resistencia: "))
   p = int(input("Digite a potencia: "))


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
   print("O resultados obtidos foram:\n")
   print(f" V={v}Volts\n P={p}Wats\n I={i}Amperes\n R={r}ohns")
   refazer=int( input("Se deseja fazer outra conta digite 0 \n Para sair digite qualquer outro numero."))
