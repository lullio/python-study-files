filmes_tuple = ("Matrix", "Matrix Reloaded", "Matrix Revolutions")
print(type(filmes_tuple))  # <class 'tuple'>

# 1 - Tamanho da tupla
print(len(filmes_tuple))  # 3    
print(f"Tamanho da tupla: {len(filmes_tuple)}")  # 3

# 2 - Recuperar item da tupla pelo índice
print(filmes_tuple[0])  # Matrix
print(filmes_tuple[:2])  # ('Matrix', 'Matrix Reloaded')

# 3 - Recuperar item da tupla pelo nome
print(filmes_tuple.index("Matrix"))  # 0
print(filmes_tuple.index("Matrix Reloaded"))  # 1

# 4 - Verificar se a tupla é vazia
print(len(filmes_tuple) == 0)  # False (a tupla não é vazia)
# 5 - Verificar se a tupla é imutável
print(isinstance(filmes_tuple, tuple))  # True (tuplas são imutáveis)

# 6 - Verificar se um item está na tupla
print("Matrix" in filmes_tuple)  # True
print("Avatar" in filmes_tuple)  # False

# 7 - Copiar a tupla
filmes_tuple_copia = filmes_tuple  # Tuplas são imutáveis, então a cópia é feita por referência
print(filmes_tuple_copia)  # ('Matrix', 'Matrix Reloaded', 'Matrix Revolutions')

# 8 - Contar quantas vezes um item aparece na tupla
print(filmes_tuple.count("Matrix"))  # 1
print(filmes_tuple.count("Avatar"))  # 0

# 9 - Obter o maior e o menor item da tupla (considerando ordem alfabética)
print(max(filmes_tuple))  # Matrix Revolutions
print(min(filmes_tuple))  # Matrix

# 4 - Adicionar item à tupla (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam adição de itens após a criação, pois são imutáveis.
# 5 - Adicionar item em uma posição específica (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam adição de itens em posições específicas, pois são imutáveis.
# 6 - Ordenar a tupla (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam ordenação, pois são imutáveis.
# 7 - Inverter a tupla (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam inversão, pois são imutáveis.
# 8 - Remover item da tupla (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam remoção de itens, pois são imutáveis.
# 9 - Remover item pelo índice (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam remoção de itens pelo índice, pois são imutáveis.

# 11 - Limpar a tupla (não é possível, pois tuplas são imutáveis)
# Tuplas não suportam limpeza, pois são imutáveis.



# 15 - Obter a soma dos itens da tupla (aplicável apenas se os itens forem números)
# Tuplas não suportam soma de itens, pois são imutáveis e não são numéricas.
# 16 - Obter a média dos itens da tupla (aplicável apenas se os itens forem números)
# Tuplas não suportam média de itens, pois são imutáveis e não são numéricas.

# 19 - Verificar se a tupla é um subconjunto de outra tupla
# Tuplas não suportam verificação de subconjunto, pois são imutáveis e não possuem métodos como listas.
