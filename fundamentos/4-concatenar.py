name = input("Digite o nome do filme: ")
year_launch = int(input("Digite o ano de lançamento: "))
rating = float(input("Digite a avaliação do filme: "))   

# Alternativa 1 concatenando com vírgula
print("Nome do filme: ", name)
# Alternativa 2 concatenando com mais
print("Nome do filme: " + name)
# Alternativa 3 concatenando com f-string, parecido com o template string do JavaScript
print(f"Nome do filme: {name}")
# Alternativa 4 concatenando com format
print("Nome do filme: {}".format(name))

# Exemplo de concatenação de strings com mais
print("O filme " + name + " foi lançado em " + str(year_launch) + " e tem uma avaliação de " + str(rating) + ".")

# Exemplo de concatenação de strings com f-string
print(f"Nome do filme: {name} \n"
      f"Lançamento: {year_launch}\n"
      f"Avaliação de {rating}.")