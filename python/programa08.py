# Operadores lógico
# AND - TODAS AS EXPRESSÕES VERDADEIRAS
# OR - PELO MENOS 1 EXPRESSÃO VERDADEIRA
# NOT - INVERTER EXPRESÃO

sou = input("Digite M/F: ")
idade = int(input("Idade: "))

if(sou == "M" and idade >= 18):
    print("Deve tirar a resevista!")


estado = input("Digite seu estado: ")    

if(estado == "piaui" or estado == "bahia"):
    print("Atende!")

doente =True

if(not doente):
    print("Acesso liberado!")