lista_filmes = ["Inception", "Interstellar", "Dunkirk", "Tenet", "The Dark Knight"]

# 1 - Tamanho da lista
print(len(lista_filmes))  # 5
print(f"Tamanho da lista: {len(lista_filmes)}")  # 5

# 2 - Recuperar item da lista pelo índice
print(lista_filmes[0])  # Inception
print(lista_filmes[1])  # Interstellar

# 3 - Recuperar item da lista pelo nome
print(lista_filmes.index("Interstellar"))  # 1
print(lista_filmes.index("Dunkirk"))  # 2

# 4- Adicionar item ao final da lista
lista_filmes.append("The Prestige")
print(lista_filmes)  # ['Inception', 'Interstellar', 'Dunkirk', 'Tenet', 'The Dark Knight', 'The Prestige']

# 5 - Adicionar item em uma posição específica
lista_filmes.insert(2, "Memento")
print(lista_filmes)  # ['Inception', 'Interstellar', 'Memento', 'Dunkirk', 'Tenet', 'The Dark Knight', 'The Prestige']

# 6 - Ordenar a lista
lista_filmes.sort()
print(lista_filmes)  # ['Dunkirk', 'Inception', 'Interstellar', 'Memento', 'Tenet', 'The Dark Knight', 'The Prestige']

# 7 - Inverter a lista
lista_filmes.reverse()
print(lista_filmes)  # ['The Prestige', 'The Dark Knight', 'Tenet', 'Memento', 'Interstellar', 'Inception', 'Dunkirk']

# 8 - Remover item da lista
lista_filmes.remove("Memento")
print(lista_filmes)  # ['The Prestige', 'The Dark Knight', 'Tenet', 'Interstellar', 'Inception', 'Dunkirk']

# 9 - Remover item pelo índice
lista_filmes.pop(0)  # Remove o primeiro item
print(lista_filmes)  # ['The Dark Knight', 'Tenet', 'Interstellar', 'Inception', 'Dunkirk']

# 10 - Verificar se um item está na lista
print("Inception" in lista_filmes)  # True
print("Avatar" in lista_filmes)  # False

# 11 - Limpar a lista
lista_filmes.clear()
print(lista_filmes)  # []

# 12 - Copiar a lista
lista_filmes = ["Inception", "Interstellar", "Dunkirk", "Tenet", "The Dark Knight"]
lista_filmes_copia = lista_filmes.copy()
print(lista_filmes_copia)  # ['Inception', 'Interstellar', 'Dunkirk', 'Tenet', 'The Dark Knight']

# 13 - Contar quantas vezes um item aparece na lista
print(lista_filmes.count("Inception"))  # 1
print(lista_filmes.count("Avatar"))  # 0

# 14 - Obter o maior e o menor item da lista (considerando ordem alfabética)
print(max(lista_filmes))  # The Dark Knight
print(min(lista_filmes))  # Dunkirk

# 15 - Obter a soma dos itens da lista (aplicável apenas se os itens forem números)
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))  # 15

# Obter a média dos itens da lista (aplicável apenas se os itens forem números)
print(sum(numeros) / len(numeros))  # 3.0

# Encontrar o índice do primeiro item que atende a uma condição
print(next((i for i, x in enumerate(numeros) if x > 3), None))  # 3 (índice do primeiro número maior que 3)