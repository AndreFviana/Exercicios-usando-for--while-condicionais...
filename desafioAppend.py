#adicionando e removendo elementos do array
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']
#subtituindo elementos do array 
lista_produtos[1]='Rímel'
lista_produtos[4]='Cremes Hidratantes'
#removendo o último elemento do array
lista_produtos.pop()

print(f'Temos {lista_produtos} à venda!')

#DESAFIO: adicionando novos elementos no array usando APPEND()
lista_produtos.append('gel para cabelo')
lista_produtos.append('cortador de unha')
print(lista_produtos)