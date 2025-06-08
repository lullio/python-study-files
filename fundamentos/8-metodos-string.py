movie_name = "Homem Aranha"

print(movie_name.upper())  # HOMEM ARANHA (converte toda a string para maiúsculas)
print(movie_name.lower())  # homem aranha (converte toda a string para minúsculas)
print(movie_name.title())  # Homem Aranha (converte a primeira letra de cada palavra para maiúscula)
print(movie_name.capitalize())  # Homem aranha (converte a primeira letra da string para maiúscula e o restante para minúsculas)
print(movie_name.swapcase())  # hOMEM aRANHA (inverte maiúsculas e minúsculas)



print(movie_name.center(10, '-')) # --Homem Aranha-- (centraliza a string em um espaço de 10 caracteres, preenchendo com '-')
print(movie_name.ljust(20, '-'))  # Homem Aranha------- (alinha à esquerda em um espaço de 20 caracteres, preenchendo com '-')
print(movie_name.rjust(20, '-'))  # -------Homem Aranha (alinha à direita em um espaço de 20 caracteres, preenchendo com '-')


print(movie_name.strip())  # Homem Aranha (remove espaços no início e no final da string)
print(movie_name.lstrip())  # Homem Aranha (remove espaços no início da string)
print(movie_name.rstrip())  # Homem Aranha (remove espaços no final da string)


print(movie_name.find("Aranha"))  # 5 (encontra a posição da substring "Aranha" na string)
print(movie_name.index("Aranha"))  # 5 (encontra a posição da substring "Aranha" na string, lança erro se não encontrar)

print(movie_name.count("a"))  # 2 (conta quantas vezes a letra "a" aparece na string)

print(movie_name.replace("Aranha", "Homem"))  # Homem Homem (substitui "Aranha" por "Homem")

print(movie_name.split())  # ['Homem', 'Aranha'] (divide a string em uma lista de palavras)
print(movie_name.split(" "))  # ['Homem', 'Aranha'] (divide a string em uma lista de palavras usando espaço como separador)
print(movie_name.split("a"))  # ['Homem ', 'r', 'nh', ''] (divide a string em uma lista de palavras usando "a" como separador)

print(movie_name.join(["Homem", "Aranha"]))  # Homem AranhaHomem Aranha (junta uma lista de strings em uma única string usando "Homem Aranha" como separador)



print(movie_name.startswith("Homem"))  # True (verifica se a string começa com "Homem")
print(movie_name.endswith("Aranha"))  # True (verifica se a string termina com "Aranha")

print(movie_name.isalpha())  # False (verifica se a string contém apenas letras)
print(movie_name.isalnum())  # False (verifica se a string contém apenas letras e números)
print(movie_name.isdigit())  # False (verifica se a string contém apenas dígitos)
print(movie_name.islower())  # False (verifica se a string está toda em minúsculas)
print(movie_name.isupper())  # False (verifica se a string está toda em maiúsculas)
print(movie_name.isspace())  # False (verifica se a string contém apenas espaços)
print(movie_name.isnumeric())  # False (verifica se a string contém apenas números)
print(movie_name.istitle())  # True (verifica se a string está em formato de título, ou seja, a primeira letra de cada palavra é maiúscula)
print(movie_name.isidentifier())  # False (verifica se a string é um identificador válido em Python)
print(movie_name.isdecimal())  # False (verifica se a string contém apenas números decimais) 
