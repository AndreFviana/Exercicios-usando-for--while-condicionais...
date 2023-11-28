#Recebi um array com o nome de vários artistas. Para saber quantas pessoas tem nessa lista eu usei a função len()
lista_musicos = [ 'Djavan','Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa']
totalDeArtistas=len(lista_musicos)
#abaixo, foi utilizado a função FORMAT, onde vc coloca um 'f' antes da string e a variavel dentro das chaves.
print(f'O total de artistas é: {totalDeArtistas}!')
#Para imprimir um item do array, veja o codigo abaixo
print(lista_musicos[14])
