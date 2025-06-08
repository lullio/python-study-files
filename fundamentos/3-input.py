# Utilizando o input
name = input("Digite o nome do filme: ")
print(name)

year_launch = input("Digite o ano de lançamento: ")
print(type(year_launch)) # input sempre retorna uma string

# convertendo o ano de lançamento para inteiro
year_launch = int(input("Digite o ano de lançamento: ")) 
print(year_launch)

# convertendo a avaliação para float
rating = float(input("Digite a avaliação do filme: "))
print(type(rating))