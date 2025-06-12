# 1 - Função para imprimir uma mensagem
def welcome():
   print("Bem-vindo ao sistema de filmes!")
welcome() # executando a função

# 2- Função para imprimir uma mensagem personalizada (usa parâmetro)   
def print_message(message):
    print(message)
print_message("Olá, usuário!")  # passando uma mensagem para a função (argumento)

# 3 - Função para somar dois números (usa parâmetros e retorna o resultado)
def sum_numbers(a, b):
    return a + b
result = sum_numbers(5, 3)  # passando dois números para a função (argumentos)
print(f"A soma é: {result}")  # imprimindo o resultado da soma

# 4 - Função para verificar se um número é par ou ímpar (usa parâmetro e retorna um valor booleano)
def is_even(number):
    return number % 2 == 0
number = 10
if is_even(number):  # passando um número para a função (argumento)
    print(f"{number} é par.")
else:
    print(f"{number} é ímpar.")

# 5 - Função para calcular a média de uma lista de números (usa parâmetro e retorna o resultado)
def calculate_average(numbers):
    if not numbers:  # Verifica se a lista está vazia
        return 0
    return sum(numbers) / len(numbers)
numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)  # passando uma lista de números para a função (argumento)  
print(f"A média é: {average}")  # imprimindo o resultado da média

def calculate_average2(qty_numbers):
   total = 0
   if not qty_numbers:
      return 0
   for i in range(qty_numbers):
      note = float(input(f"Digite a nota/número {i+1}: "))
      total += note
   return print(f"A média de {total} por {qty_numbers} é: {total / qty_numbers}")
calculate_average2(5)
   

# 6 - Função para verificar se um item está em uma lista (usa parâmetros e retorna um valor booleano)
def item_in_list(item, lst):
    return item in lst
item = "Matrix"
movies_list = ["Matrix", "Inception", "Interstellar"]
if item_in_list(item, movies_list):  # passando um item e uma lista para a função (argumentos)
    print(f"{item} está na lista de filmes.")
else:
    print(f"{item} não está na lista de filmes.")  

# 7 - Função para imprimir todos os filmes de uma lista (usa parâmetro)
def print_movies(movies):
    for movie in movies:  # Itera sobre a lista de filmes
        print(movie) 
movies_list = ["Matrix", "Inception", "Interstellar"]
print_movies(movies_list)  # passando uma lista de filmes para a função (argumento)

# 8 - Função com parâmetro default
def greet(name="usuário"):
    print(f"Olá, {name}!")  # Imprime uma saudação com o nome fornecido ou o padrão "usuário"
greet()  # Chama a função sem passar um nome, usando o valor padrão  
greet("Alice")  # Chama a função passando um nome específico
# 9 - Função com múltiplos parâmetros
def multiply(a, b=1, c=1):
    return a * b * c  # Multiplica os três parâmetros 
result = multiply(2, 3)  # Passa dois parâmetros, o terceiro usa o valor padrão
print(f"O resultado da multiplicação é: {result}")  # Imprime o resultado da multiplicação      

# 10 - Função com retorno de múltiplos valores
def get_movie_info(title, year):
    return title, year  # Retorna o título e o ano do filme como uma tupla
movie_title, movie_year = get_movie_info("Inception", 2010)  # Recebe os valores retornados
print(f"Filme: {movie_title}, Ano: {movie_year}")  # Imprime o título e o ano do filme 