#programa que calcule duas médias e veja se o aluno foi aprovado ou não 
# >= 7 aprovado 
# <= 6 reprovado

med1 = float(input("Digite sua primeira nota: "))
med2 = float(input("Digite sua segunda nota: "))

result = (med1 + med2) / 2
if(result >= 7):
    print("Aprovado")
else:
    print("Reprovado")
