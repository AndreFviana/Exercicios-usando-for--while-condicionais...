#CALCULADORA DE IMC
peso = int(input('Qual o seu peso?')) 
altura = float(input('Qual o sua altura?')) 
def calcularImc(peso,altura):
  imc=peso/(altura*altura)
  if(imc <=16.9):
    return( 'Muito abaixo do peso')
  elif( imc>= 17) and (imc<=18.4):
    return( 'Abaixo do peso')
  elif( imc >=18.5) and (imc <=24.9):
    return( 'Peso normal')
  elif( imc >=25) and (imc<=29.9):
     return( ' Acima do peso')
  elif( imc >=30) and (imc<=34.9):
    return( 'Obesidade grau I')
  elif( imc>=35) and (imc<=40):
     return( 'Obesidade grau II')
  else :
    return( 'Obesidade grau III')
   
resultadoImc=calcularImc(peso,altura)
print(resultadoImc)