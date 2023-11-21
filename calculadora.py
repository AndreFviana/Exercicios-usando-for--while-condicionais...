#CALCULADORA 
num1=int(input('Digite um nùmero'))
num2=int(input('Digite outro nùmero'))
def calcular(num1,num2,operacao):
  if operacao == 1:
    return num1 + num2
  elif operacao == 2:
    return num1 - num2
  elif operacao == 3:
    return num1 * num2
  elif operacao == 4:
    return num1 / num2
  else:
    return 0
total= calcular(10,10,2)
print(total)