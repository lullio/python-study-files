# Função lambda é uma função anônima, ou seja, não possui um nome definido. É usada para criar funções pequenas e simples de forma rápida.

# Função de potência de um número
potencia = lambda num: num ** 2  # Define uma função lambda para calcular a potência
print(potencia(5))  # Chama a função lambda e imprime o resultado (25)

# Função de soma de dois números
soma = lambda a, b: a + b  # Define uma função lambda para somar dois números
print(soma(3, 4))  # Chama a função lambda e imprime o resultado (7)

# Função de verificação de paridade
paridade = lambda x: "Par" if x % 2 == 0 else "Ímpar"  # Define uma função lambda para verificar se um número é par ou ímpar
is_even = lambda x: x % 2 == 0  # Define uma função lambda para verificar se um número é par
print(paridade(10))  # Chama a função lambda e imprime o resultado ("Par")

# Função de filtragem de números pares em uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números
pares = list(filter(lambda x: x % 2 == 0, numeros))  # Usa filter com uma função lambda para filtrar números pares
print(pares)  # Imprime a lista de números pares ([2, 4, 6, 8, 10])

# Função que divide um número por outro
divisao = lambda x, y: x / y if y != 0 else "Divisão por zero"  # Define uma função lambda para dividir dois números
print(divisao(10, 2))  # Chama a função lambda e imprime o resultado (5.0)
print(divisao(10, 0))  # Chama a função lambda e imprime o resultado ("Divisão por zero")

# Funcionalidades relacionadas aos filmes
movies_list = ["Matrix", "Matrix Reloaded", "Matrix Revolutions", "Titanic"]  # Lista de filmes
ratings = {
      "Matrix": [8.5, 9.0, 8.7],
      "Matrix Reloaded": [7.5, 8.0, 7.8],
      "Matrix Revolutions": [6.5, 7.0, 6.8],
      "Titanic": [9.5, 9.0, 9.2]
}
# Função para calcular a média de avaliações de um filme
average_rating = lambda movie: sum(ratings[movie]) / len(ratings[movie]) if movie in ratings else 0  # Define uma função lambda para calcular a média de avaliações
print(average_rating("Matrix"))  # Chama a função lambda e imprime a média de avaliações (8.733333333333333)
print(average_rating("Titanic"))  # Chama a função lambda e imprime a média de avaliações (9.233333333333333)

# Função que verifica se um filme está na lista
is_movie_in_list = lambda movie: movie in movies_list  # Define uma função lambda para verificar se um filme está na lista
print(is_movie_in_list("Matrix"))  # Chama a função lambda e imprime o resultado (True)
print(is_movie_in_list("Avatar"))  # Chama a função lambda e imprime o resultado (False)

# Função para recomendar um filme com base na média de avaliações
recommend_movie = lambda: max(movies_list, key=average_rating)  # Define uma função lambda para recomendar um filme com base na média de avaliações

recommend_movie2 = lambda movie: f"Recomendo assistir '{movie}' com média de avaliações {average_rating(movie):.2f}" # Define uma função lambda para recomendar um filme com base na média de avaliações
print(f"Recomendação: {recommend_movie()}")  # Chama a função lambda e imprime a recomendação
# copilot ajude aqui