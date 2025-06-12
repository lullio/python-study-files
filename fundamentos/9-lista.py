filme_matrix = []
print(type(filme_matrix))  # <class 'list'>

# Adicionando filmes à lista
filme_matrix.append("Matrix")
print(filme_matrix)  # ['Matrix']

filme_matrix.append("Matrix Reloaded")
print(filme_matrix)  # ['Matrix', 'Matrix Reloaded']


dados_filme_matrix = ["Matrix", 1999, 8.7, True]
print(dados_filme_matrix)  # ['Matrix', 1999, 8.7, True]
filme_matrix.append(dados_filme_matrix)
print(filme_matrix)  # ['Matrix', 'Matrix Reloaded', ['Matrix', 1999, 8.7, True]]



lista_filmes = ["Matrix", "Matrix Reloaded", "Matrix Revolutions"]
print(lista_filmes)  # ['Matrix', 'Matrix Reloaded', 'Matrix Revolutions']

# 1 - Buscar os dois primeiros filmes
print(lista_filmes[:2])  # ['Matrix', 'Matrix Reloaded']

# 2 - Buscar o último filme
print(lista_filmes[-1])  # Matrix Revolutions

# 3 - Buscar filmes até uma certa posição
print(lista_filmes[:3])  # ['Matrix', 'Matrix Reloaded']

# 4 - Buscar o primeiro filme
print(lista_filmes[0])  # Matrix

# 4 - Buscar o primeiro e o segundo filme
print(lista_filmes[0:2])  # ['Matrix', 'Matrix Reloaded']

# 5 - Buscar o segundo e o terceiro filme
print(lista_filmes[1:3])  # ['Matrix Reloaded', 'Matrix Revolutions']

# 6 - Buscar o primeiro e o terceiro filme
print(lista_filmes[0:3:2])  # ['Matrix', 'Matrix Revolutions']
