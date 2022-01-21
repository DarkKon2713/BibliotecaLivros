print("Bem vindo a sua Biblioteca")

while True:
    inicial=input("Para logar Digite S e para criar usuario digite N.\n")
    if (inicial=="S") or(inicial=="s"): #Logar
        usuario=input("Digite seu usuario:")
        arquivo=open(f"{usuario}.txt","r")
                                                   
        
    elif (inicial=="N") or (inicial=="n"): #criar usuario
       print("Ola")
    else: 
        print("Digite uma opção valida") #leia direito
        
       