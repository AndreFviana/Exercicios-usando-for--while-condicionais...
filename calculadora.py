#CALCULADORA 
def calculadora():
  #mostrar menu de operações
  print('escolha um número relacionado a operação')
  menu='1-> Soma, 2-> Subtração, 3-> Multiplicação, 4-> Divisão, 0-> Sair'
  print(menu)

  #estrutura de repetição para captar e armazenar dados de entrada nas variáveis
  
  while True:
    operacao=int(input())
  
    print('Agora digite um número:')
    primeiro_numero=int(input())
    print('Agora digite outro número:')
    segundo_numero=int(input())
#condicional para calcular o números de entrada e mostrar o resultado para o usuário.
    if(operacao == 1):
        resultado = primeiro_numero + segundo_numero
#na linha abaixo, converti a variável resultado em string, pois só assim é possivel concatenar str com int. 
        print('O resultado é: '+str(resultado))

    elif(operacao == 2):
        resultado = primeiro_numero - segundo_numero 
        return 'O resultado é: '+str(resultado)

    elif(operacao == 3):
        resultado = primeiro_numero * segundo_numero 
        return 'O resultado é: '+str(resultado)

    elif(operacao == 4):
        resultado = primeiro_numero / segundo_numero 
        return 'O resultado é: '+str(resultado)
    
    elif(operacao == 0):
      resultado = "Sair"
      return resultado
    else: 
      break
  
#chamando a função
calculadora()

#Teste