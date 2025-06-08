movie_name = "Top Gun"

# índice começa em 0 e vai até o tamanho da string - 1

print(movie_name[0])  # T
print(movie_name[1])  # o

# 1 - Buscar toda string a partir de um índice
print(movie_name[0:]) # Top Gun
print(movie_name[:7]) # Top Gun (até o índice 6, que é o último índice da string)§§§§§§§

# 2 - Buscar uma parte da string
print(movie_name[0:3])  # Top
print(movie_name[4:])  # Gun  

# 3 - Buscar toda a string de 2 em 2 caracteres
print(movie_name[::2])  # Quer pegar toda a string, mas com passo 2 (ou seja, pega cada segundo caractere)
# Resultado: TpG (T, p, G) 
print(movie_name[0:7:2])  # TpG

# 4 - Buscar toda a string nos indices impares
print(movie_name[1::2])  # o u (começa do índice 1 e pega cada segundo caractere a partir daí)

# 5 - Inverter uma string de trás para frente
print(movie_name[::-1])  # nuG poT (inverte a string)

print(movie_name[6:0:-1])  # nuG poT (começa do índice 6 e vai até o índice 1, invertendo a string)
