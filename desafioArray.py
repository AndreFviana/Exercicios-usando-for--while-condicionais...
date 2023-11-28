#Uma nova loja de cosméticos abriu no seu bairro e pediram para você elaborar um sistema que imprime na tela na frente da loja os novos produtos que chegaram. O sistema da loja já tem um array com os produtos, você precisa apenas imprimir eles no terminal, um por um.

#imprimindo todos os arrays de um por um
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
print(lista_produtos[0])
print(lista_produtos[1])
print(lista_produtos[2])
print(lista_produtos[3])
print(lista_produtos[4])
print(lista_produtos[5])
print(lista_produtos[6])
print(lista_produtos[7])

#Agora, imprimindo com uma mensagem
print(f'Temos {lista_produtos[0]} à venda!')
print(f'Temos {lista_produtos[1]} à venda!')
print(f'Temos {lista_produtos[2]} à venda!')
print(f'Temos {lista_produtos[3]} à venda!')
print(f'Temos {lista_produtos[4]} à venda!')
print(f'Temos {lista_produtos[5]} à venda!')
print(f'Temos {lista_produtos[6]} à venda!')
print(f'Temos {lista_produtos[7]} à venda!')

#uma melhoria seria usar um FOR para repetir tudo isso
for i in range(len(lista_produtos)):
  print(f'Temos {lista_produtos[i]}!')