from typing import List


agenda = []


def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    print(f"Nome:{nome} Telefone:{telefone}")


def pede_nome_arquivo():
    nomearquivo=input("Nome do arquivo: ")
    return nomearquivo+".txt"


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    global agenda
    nome = pede_nome()
    telefone=pede_telefone()
    agenda.append([nome,telefone])
def apaga():
    global agenda
    nome=pede_nome()
    p=pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome não encontrado.")
def altera():
    p= pesquisa(pede_nome())
    if p is not None:
        nome=agenda[p][0]
        telefone=agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome,telefone)
        nome=pede_nome()
        telefone=pede_telefone()
        agenda[p]=[nome, telefone]
    else: 
        print("Nome não encontrado.")
        
def lista():
    print("\nAgenda\n\n----------")
    for e in agenda:
        mostra_dados(e[0],e[1])
    print("----\n")
    
def le():
    global agenda
    nome_arquivo= pede_nome_arquivo()
    try:
        with open(nome_arquivo,"r",encoding="utf-8") as arquivo:
            agenda=[]
            for l in arquivo.readlines():
                nome,telefone= l.strip().split("#")
                agenda.append([nome,telefone])
    except:
        print("\nObjeto não encontrado\n")
        
def grava():
    nome_arquivo=pede_nome_arquivo()
    with open(nome_arquivo,"w",encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor= int(input(pergunta))
            if inicio<=valor<=fim:
                return valor
        except ValueError:
            print(f"Valor invalido, favor digitar entre{inicio} e {fim}.")
def menu():
    print("""
          1-Novo
          2_Altera
          3-Apaga
          4-lista
          5-Grava
          6-Le
          
          0-Sair
          """)
    return valida_faixa_inteiro("Escolha uma opçao:",0,6)
while True:
    opcao=menu()
    if opcao==0:
        break
    elif opcao==1:
        novo()
    elif opcao==2:
        altera()
    elif opcao==3:
        apaga()
    elif opcao==4:
        lista()
    elif opcao==5:
        grava()
    elif opcao==6:
        le()
    
