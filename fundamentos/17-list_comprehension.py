# 1 - Listando valores de 0 a 10 que sejam menores do que 4
for i in range(10):
   if i < 4:
      print(i)

# Solução usando list comprehension
# O código abaixo cria uma lista com os números de 0 a 9 que são menores que 4.
# A list comprehension é uma forma concisa de criar listas em Python em uma única linha.
# A sintaxe é: [expressão for item in iterável if condição]
lista_menores_que_quatro = [i for i in range(10) if i < 4]

# Lista de filmes
lista_filmes = ["Matrix", "Matrix Reloaded", "Matrix Revolutions", "The Matrix Resurrections", "Avatar", "Inception"]

# 2 - Listando filmes que começam com 'M'
lista_filmes_com_m = [filme for filme in lista_filmes if filme.startswith("M")]
print(lista_filmes_com_m)
# A list comprehension acima cria uma lista contendo apenas os filmes que começam com a letra 'M'.

lista_filmes_com_e = [movie for movie in lista_filmes if 'e' in movie.lower()]
print(lista_filmes_com_m)
# A list comprehension acima cria uma lista contendo apenas os filmes que contêm a letra 'e' (independente de ser maiúscula ou minúscula).

# 3 - Listando filmes que têm mais de 10 caracteres
lista_filmes_maior_que_dez = [filme for filme in lista_filmes if len(filme) > 10]
print(lista_filmes_maior_que_dez)
# A list comprehension acima cria uma lista contendo apenas os filmes que têm mais de 10 caracteres.

# 4 - Listando filmes que têm entre 10 e 20 caracteres
lista_filmes_entre_dez_e_vinte = [filme for filme in lista_filmes if 10 < len(filme) < 20]
print(lista_filmes_entre_dez_e_vinte)
# A list comprehension acima cria uma lista contendo apenas os filmes que têm entre 10 e 20 caracteres.

# 5 - Filmes que eu gostaria de assistir
lista_filmes_que_gostaria_de_assistir = [filme for filme in lista_filmes if filme not in ["Avatar", "Inception"]]
lista_filmes_que_gostaria_de_assistir = [filme for filme in lista_filmes if filme != "Avatar" and filme != "Inception"] # Outra forma de fazer a mesma coisa

# 6 - Encontrando o filme pelo nome
while True:
   searchName = input("Digite o nome do filme que você está procurando(ou sair para encerrar): ")
   if searchName.lower() == "sair":
      print("Encerrando a busca.")
      break
   foundMovies = [movie for movie in lista_filmes if searchName.lower() in movie.lower()]
   if foundMovies:
      print(f"Filmes encontrados: {foundMovies}")
      for movie in foundMovies:
         print(f"Você encontrou o filme: {movie}")
   else:
      print(f"Nenhum filme encontrado com o nome '{searchName}'.")