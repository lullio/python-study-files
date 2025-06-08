# Python é case sensitive
movie_1 = "Homem aranha"
movie_2 = "homem aranha"

print(f"Comparando {movie_1} e {movie_2}: {movie_1 == movie_2}") # False
print(f"Comparando {movie_1} e {movie_2} com lower(): {movie_1.lower() == movie_2.lower()}") # True

movie_description = """
O filme é muito bom
É o meu filme predileto rsrs
      Teste de posicionamento do texto
"""
print(movie_description)

# 1 - Multiplicação de strings
print("Python " * 3)  # Python Python Python
print("=" * 20) # ====================

# 2 - Verificando o tamanho da string
print(f"Tamanho da string '{movie_1}': {len(movie_1)}")  # 12
print(f"Tamanho da string '{movie_description}': {len(movie_description)}")  # 60

# 3 - Verificando se a string começa ou termina com uma substring
print(f"'{movie_1}' começa com 'Homem': {movie_1.startswith('Homem')}")  # True
print(f"'{movie_1}' termina com 'anha': {movie_1.endswith('anha')}")  # True  

# 4 - Verificando se a string contém uma substring
print(f"'{movie_1}' contém 'aranha': {'aranha' in movie_1}")  # True

# 5 - Convertendo para maiúsculas e minúsculas
print(f"'{movie_1}' em maiúsculas: {movie_1.upper()}")  # HOMEM ARANHA
print(f"'{movie_1}' em minúsculas: {movie_1.lower()}")  # homem aranha

# 6 - Substituindo partes da string
print(f"Substituindo 'aranha' por 'homem': {movie_1.replace('aranha', 'homem')}")  # Homem homem

# 7 - Dividindo a string em uma lista
print(f"Dividindo '{movie_1}' em palavras: {movie_1.split()}")  # ['Homem', 'aranha']  

# 8 - Juntando uma lista de strings em uma única string
words = ['Homem', 'aranha']
print(f"Juntando palavras: {' '.join(words)}")  # Homem aranha

# 9 - Verificando se a string é alfanumérica
print(f"'{movie_1}' é alfanumérica? {movie_1.isalnum()}")  # False (contém espaço)  

# 10 - Verificando se a string é numérica
print(f"'{movie_1}' é numérica? {movie_1.isnumeric()}")  # False (contém letras)

# 11 - Verificando se a string é composta apenas por letras
print(f"'{movie_1}' é composta apenas por letras? {movie_1.isalpha()}")  # False (contém espaço)

# 12 - Verificando se a string é composta apenas por espaços
print(f"'{movie_1}' é composta apenas por espaços? {movie_1.isspace()}")  # False (contém letras)

# 13 - Verificando se a string é um título (primeira letra de cada palavra maiúscula)
print(f"'{movie_1}' é um título? {movie_1.istitle()}")  # True (primeira letra de cada palavra maiúscula)

# 14 - Verificando se a string é um dígito
print(f"'{movie_1}' é um dígito? {movie_1.isdigit()}")  # False (contém letras)

# 15 - Verificando se a string é um identificador válido
print(f"'{movie_1}' é um identificador válido? {movie_1.isidentifier()}")  # False (contém espaço)
 
# 16 - Verificando se a string é um espaço em branco
print(f"'{movie_1}' é um espaço em branco? {movie_1.isspace()}")  # False (contém letras)
# 17 - Verificando se a string é um número decimal
print(f"'{movie_1}' é um número decimal? {movie_1.isdecimal()}")  # False (contém letras)
# 18 - Verificando se a string é um número hexadecimal
print(f"'{movie_1}' é um número hexadecimal? {movie_1.ishexadecimal()}")  # False (contém letras)
# 19 - Verificando se a string é um número octal
print(f"'{movie_1}' é um número octal? {movie_1.isoctal()}")  # False (contém letras)
# 20 - Verificando se a string é um número binário
print(f"'{movie_1}' é um número binário? {movie_1.isbinary()}")  # False (contém letras)
# 21 - Verificando se a string é um número complexo
print(f"'{movie_1}' é um número complexo? {movie_1.iscomplex()}")  # False (contém letras)
# 22 - Verificando se a string é um número real
print(f"'{movie_1}' é um número real? {movie_1.isreal()}")  # False (contém letras)
# 23 - Verificando se a string é um número inteiro
print(f"'{movie_1}' é um número inteiro? {movie_1.isinteger()}")  # False (contém letras)
# 24 - Verificando se a string é um número racional
print(f"'{movie_1}' é um número racional? {movie_1.isrational()}")  # False (contém letras)
# 25 - Verificando se a string é um número irracional
print(f"'{movie_1}' é um número irracional? {movie_1.isirrational()}")  # False (contém letras)
# 26 - Verificando se a string é um número primo
print(f"'{movie_1}' é um número primo? {movie_1.isprime()}")  # False (contém letras)
# 27 - Verificando se a string é um número composto
print(f"'{movie_1}' é um número composto? {movie_1.iscomposite()}")  # False (contém letras)
# 28 - Verificando se a string é um número perfeito
print(f"'{movie_1}' é um número perfeito? {movie_1.isperfect()}")  # False (contém letras)
# 29 - Verificando se a string é um número abundante
print(f"'{movie_1}' é um número abundante? {movie_1.isabundant()}")  # False (contém letras)
# 30 - Verificando se a string é um número deficiente
print(f"'{movie_1}' é um número deficiente? {movie_1.isdeficient()}")  # False (contém letras)
# 31 - Verificando se a string é um número amigável
print(f"'{movie_1}' é um número amigável? {movie_1.isamicable()}")  # False (contém letras)
# 32 - Verificando se a string é um número semiperfeito
print(f"'{movie_1}' é um número semiperfeito? {movie_1.issemiperfect()}")  # False (contém letras)
# 33 - Verificando se a string é um número triangular
print(f"'{movie_1}' é um número triangular? {movie_1.istriangular()}")  # False (contém letras)
# 34 - Verificando se a string é um número quadrado
print(f"'{movie_1}' é um número quadrado? {movie_1.issquare()}")  # False (contém letras)
# 35 - Verificando se a string é um número cúbico
print(f"'{movie_1}' é um número cúbico? {movie_1.iscube()}")  # False (contém letras)
# 36 - Verificando se a string é um número pentagonal
print(f"'{movie_1}' é um número pentagonal? {movie_1.ispentagonal()}")  # False (contém letras)
# 37 - Verificando se a string é um número hexagonal
print(f"'{movie_1}' é um número hexagonal? {movie_1.ishexagonal()}")  # False (contém letras)
# 38 - Verificando se a string é um número heptagonal
print(f"'{movie_1}' é um número heptagonal? {movie_1.isheptagonal()}")  # False (contém letras)
# 39 - Verificando se a string é um número octagonal
print(f"'{movie_1}' é um número octagonal? {movie_1.isoctagonal()}")  # False (contém letras)
# 40 - Verificando se a string é um número nonagonal
print(f"'{movie_1}' é um número nonagonal? {movie_1.isnonagonal()}")  # False (contém letras)
# 41 - Verificando se a string é um número decagonal
print(f"'{movie_1}' é um número decagonal? {movie_1.isdecagonal()}")  # False (contém letras)
# 42 - Verificando se a string é um número dodecagonal
print(f"'{movie_1}' é um número dodecagonal? {movie_1.isdodecagonal()}")  # False (contém letras)
# 43 - Verificando se a string é um número icosaédrico
print(f"'{movie_1}' é um número icosaédrico? {movie_1.isicosahedral()}")  # False (contém letras)
# 44 - Verificando se a string é um número dodecaédrico
print(f"'{movie_1}' é um número dodecaédrico? {movie_1.isdodecahedral()}")  # False (contém letras)
# 45 - Verificando se a string é um número poligonal
print(f"'{movie_1}' é um número poligonal? {movie_1.ispolygonal()}")  # False (contém letras)
# 46 - Verificando se a string é um número figurado
print(f"'{movie_1}' é um número figurado? {movie_1.isfigured()}")  # False (contém letras)
# 47 - Verificando se a string é um número de Fibonacci  
print(f"'{movie_1}' é um número de Fibonacci? {movie_1.isfibonacci()}")  # False (contém letras)
# 48 - Verificando se a string é um número primo de Mersenne
print(f"'{movie_1}' é um número primo de Mersenne? {movie_1.ismersenneprime()}")  # False (contém letras)
# 49 - Verificando se a string é um número primo de Fermat
print(f"'{movie_1}' é um número primo de Fermat? {movie_1.isfermatprime()}")  # False (contém letras)
# 50 - Verificando se a string é um número primo de Sophie Germain
print(f"'{movie_1}' é um número primo de Sophie Germain? {movie_1.issophiegermainprime()}")  # False (contém letras)
# 51 - Verificando se a string é um número primo de Wilson
print(f"'{movie_1}' é um número primo de Wilson? {movie_1.iswilsonprime()}")  # False (contém letras)
# 52 - Verificando se a string é um número primo de Lucas
print(f"'{movie_1}' é um número primo de Lucas? {movie_1.islucasprime()}")  # False (contém letras)
# 53 - Verificando se a string é um número primo de Pell
print(f"'{movie_1}' é um número primo de Pell? {movie_1.ispellprime()}")  # False (contém letras)
