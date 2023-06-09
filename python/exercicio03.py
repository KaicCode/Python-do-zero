# Faça um programa que calcule o desconto de um produto de acordo com a forma de pagamento
# A vista 10%
# Cartão 5%
# Parcela normal

valor = float(input("Digite o valor do produto: "))
desconto = int(input("1 - A vista 10%\n 2 - Cartão 5%\n 3 -Parcela normal\n "))
if(desconto == 1):
    10 * valor / 100
    print("Desconto foi de: ")
    if(desconto == 2):
        5 * valor / 100
    print("Desconto foi de: ")
    if(desconto == 3):
          print("Não tem desconto")
