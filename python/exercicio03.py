# Faça um programa que calcule o desconto de um produto de acordo com a forma de pagamento
# A vista 10%
# Cartão 5%
# Parcela normal

valor = float(input("Digite o valor do produto: "))
desconto = int(input("1 - A vista 10%\n 2 - Cartão 5%\n 3 -Parcela normal\n "))
if(desconto == 1):
    cal = valor * 0.90
    print(f"Desconto foi de:{cal}")
    if(desconto == 2):
      cal = valor * 0.95
    print(f"Desconto foi de:{cal}")
    if(desconto == 3):
          print("Não tem desconto")
