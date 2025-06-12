"""
*args - Utilizado para passar um número variável de argumentos posicionais para uma função.
- Os argumentos são empacotados em uma tupla dentro da função, permitindo que você passe quantos argumentos quiser.
- Usar quando você não sabe quantos argumentos serão passados para a função ou quando deseja permitir que o usuário forneça uma lista de valores.
"""

# 1 - Soma de vários números usando *args
def sum_numbers(*args):
    total = 0
    for num in args:  # Itera sobre os números passados como argumentos
        total += num
    return total
print(sum_numbers(1, 2, 3, 4, 5))  # Passa múltiplos números como argumentos

# 2 - Função que recebe uma lista de números e retorna a soma usando *args
def sum_list(*args):
    return sum(args)  # Usa a função built-in sum para somar os números
print(sum_list(10, 20, 30))  # Passa múltiplos números como argumentos


# 3 - Função que recebe uma lista de strings e retorna a concatenação usando *args
def concatenate_strings(*args):
    return " ".join(args)  # Usa a função join para concatenar as strings com espaço
print(concatenate_strings("Olá", "mundo!", "Como", "você", "está?"))  # Passa múltiplas strings como argumentos

# 4 - Função que recebe uma lista de números e retorna o maior número usando *args
def max_number(*args):
    if not args:  # Verifica se não foram passados argumentos
        return None
    return max(args)  # Usa a função built-in max para encontrar o maior número
print(max_number(5, 10, 3, 8))  # Passa múltiplos números como argumentos

# 5 - Função com argumentos variáveis
def print_movies(*movies):
    for movie in movies:  # Itera sobre os filmes passados como argumentos
        print(movie)
print_movies("Matrix", "Inception", "Interstellar")  # Passa múltiplos filmes como argumentos

# 12 - Função com argumentos nomeados
def print_movie_info(title, year, director=None):
    info = f"Filme: {title}, Ano: {year}"
    if director:  # Verifica se o diretor foi fornecido
        info += f", Diretor: {director}"
    print(info)
print_movie_info("Inception", 2010, "Christopher Nolan")  # Passa todos os argumentos
print_movie_info("Interstellar", 2014)  # Passa apenas título e ano, sem diretor  


"""
**kwargs - Utilizado para passar um número variável de argumentos nomeados (chave-valor) para uma função.
- Os argumentos são empacotados em um dicionário dentro da função, permitindo que você passe quantos pares chave-valor quiser.
- Quando você precisar não só do valor, mas também de uma chave associada a ele, **kwargs é a escolha ideal.
"""
# 1 - Apresentação de Curso com **kwargs
def course_info(**kwargs):
    for key, value in kwargs.items():  # Itera sobre os pares chave-valor
        print(f"{key}: {value}")  # Imprime cada par chave-valor
course_info(
    title="Python para Iniciantes",
    duration="4 semanas",
    instructor="João Silva",
    level="Básico"
)  # Passa múltiplos argumentos nomeados

# 2 - Função que recebe informações de um livro usando **kwargs
def book_info(**kwargs):
    for key, value in kwargs.items():  # Itera sobre os pares chave-valor
        print(f"{key}: {value}")  # Imprime cada par chave-valor
book_info(
    title="1984",
    author="George Orwell",
    year=1949,
    genre="Ficção Científica"
)  # Passa múltiplos argumentos nomeados

# 3 - Função que recebe informações de um filme usando **kwargs
def movie_info(**kwargs):
    for key, value in kwargs.items():  # Itera sobre os pares chave-valor
        print(f"{key}: {value}")  # Imprime cada par chave-valor    
movie_info(
    title="The Matrix",
    year=1999,
    director="Lana Wachowski, Lilly Wachowski",
    genre="Sci-Fi",
    rating=8.7
)  # Passa múltiplos argumentos nomeados