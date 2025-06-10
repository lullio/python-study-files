# Lista de filmes
lista_filmes = ["Matrix", "Matrix Reloaded", "Matrix Revolutions"]
print(lista_filmes)  # ['Matrix', 'Matrix Reloaded', 'Matrix Revolutions']

# 1 - Imprimir todos os filmes fora da lista (Iterar sobre a lista)
for filme in lista_filmes:
    print(filme)
    
# 2 - Imprimir os filmes com seus índices
for index, filme in enumerate(lista_filmes):
    print(f"{index}: {filme}")

# 3 - Imprimir os filmes com seus índices e verificar se o índice é par ou ímpar
for index, filme in enumerate(lista_filmes):
    if index % 2 == 0:
        print(f"{index} (par): {filme}")
    else:
        print(f"{index} (ímpar): {filme}")
        
# 4 - Imprimir os filmes com seus índices e verificar se o índice é maior que 1
for index, filme in enumerate(lista_filmes):
    if index > 1:
        print(f"{index} (maior que 1): {filme}")
    else:
        print(f"{index} (menor ou igual a 1): {filme}")

# 5 - break - Parar a iteração quando encontrar o primeiro filme que começa com 'M'
for filme in lista_filmes:
    if filme.startswith("M"):
        print(f"Encontrado o primeiro filme que começa com 'M': {filme}")
        break

# 6 - continue - Pular o filme que começa com 'M'
for filme in lista_filmes:
    if filme.startswith("M"):
        print(f"Pulei o filme que começa com 'M': {filme}")
        continue
    print(f"Filme que não começa com 'M': {filme}")

# 7 - while - Imprimir os filmes enquanto houver filmes na lista
while lista_filmes:
    filme = lista_filmes.pop(0)  # Remove o primeiro filme da lista
    print(f"Filme removido da lista: {filme}")

# 8 - while - Imprimir os filmes enquanto houver filmes na lista, mas parar quando encontrar 'Matrix Reloaded'
lista_filmes = ["Matrix", "Matrix Reloaded", "Matrix Revolutions"]
while lista_filmes:
    filme = lista_filmes.pop(0)  # Remove o primeiro filme da lista
    if filme == "Matrix Reloaded":
        print(f"Parando a iteração ao encontrar: {filme}")
        break
    print(f"Filme removido da lista: {filme}")

"""
------------------------------------------------- WHILE
"""
# WHILE - Iterando valores de uma lista usando while
lista_filmes = ["Matrix", "Matrix Reloaded", "Matrix Revolutions"]
index = 0
while index < len(lista_filmes):
   print(lista_filmes[index])
   index+=1

# 9 - while - Imprimir os filmes enquanto houver filmes na lista, mas pular 'Matrix Reloaded'  
while lista_filmes:
    filme = lista_filmes.pop(0)  # Remove o primeiro filme da lista
    if filme == "Matrix Reloaded":
        print(f"Pulei o filme: {filme}")
        continue
    print(f"Filme removido da lista: {filme}")


# 10 - for com range - Imprimir os filmes usando range
for i in range(len(lista_filmes)):
    print(f"{i}: {lista_filmes[i]}")
# 11 - for com range e verificar se o índice é par ou ímpar

for i in range(len(lista_filmes)):
    if i % 2 == 0:
        print(f"{i} (par): {lista_filmes[i]}")
    else:
        print(f"{i} (ímpar): {lista_filmes[i]}")
        
total_avaliacoes = int(input("Quantas avaliações você deseja fazer? "))
total = 0
for i in range(total_avaliacoes):
   nota_avaliacao = float(input("Digite a avaliação: "))
   total += nota_avaliacao

if total_avaliacoes > 0:
   avaliacao_media = total / total_avaliacoes
else:
   avaliacao_media = 0

print(f"A avaliação média do filme é: {avaliacao_media}:.2f ")
