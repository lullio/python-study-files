# O código abaixo demonstra o uso de conjuntos (sets) em Python, que são coleções não ordenadas de elementos únicos.
# Sets são úteis para armazenar itens sem duplicatas e realizar operações de conjunto, como união, interseção e diferença.
# Sets são mutáveis, o que significa que você pode adicionar ou remover elementos após a criação do conjunto.

# Sets são parecidos com dicionários, mas dicionários armazenam pares de chave-valor, enquanto sets armazenam apenas valores únicos.
# Tanto em sets, quanto listas e tuplas, só tem valores, não tem chaves.

# Criando um conjunto de filmes
filmes_set = {"Matrix", "Matrix Reloaded", "Matrix Revolutions"}
filmes_set2 = set(["Matrix2", "Matrix Reloaded2", "Matrix Revolutions2"])

print(type(filmes_set))  # <class 'set'>

# Adicionando filmes ao conjunto
filmes_set.add("Matrix Resurrections")
print(filmes_set)  # {'Matrix Reloaded', 'Matrix Resurrections', 'Matrix Revolutions', 'Matrix'}


# Adicionando um filme que já existe no conjunto (não terá efeito, pois sets não permitem duplicatas)
filmes_set.add("Matrix")
print(filmes_set)  # {'Matrix Reloaded', 'Matrix Resurrections', 'Matrix Revolutions', 'Matrix'}

filmes_set.add(1, True) # TypeError: add() takes exactly one argument (2 given)

# Update do conjunto com múltiplos valores
# O método update permite adicionar múltiplos valores ao conjunto de uma vez
filmes_set.update([1, True])  # Adiciona múltiplos valores ao conjunto
print(filmes_set)  # {'Matrix Reloaded', 'Matrix Resurrections', 'Matrix Revolutions', 'Matrix', 1, True}
# O método update também pode receber outros conjuntos
filmes_set.update(filmes_set2)  # Adiciona os valores do outro conjunto
print(filmes_set)  # {'Matrix Reloaded', 'Matrix Resurrections', 'Matrix Revolutions', 'Matrix', 1, True, 'Matrix2', 'Matrix Reloaded2', 'Matrix Revolutions2'}

# Adicionando valores de diferentes tipos ao conjunto
filmes_set.add(1)
filmes_set.add(True)  # True e 1 são iguais
print(filmes_set)  # {'Matrix Reloaded', 'Matrix Resurrections', 'Matrix Revolutions', 'Matrix', 1, True}

# Verificando se um filme está no conjunto
print("Matrix" in filmes_set)  # True

# Verificando o tamanho do conjunto
print(len(filmes_set))  # 4 (o tamanho do conjunto é 4, pois "Matrix" só conta uma vez)

# Removendo um filme do conjunto
filmes_set.remove("Matrix Reloaded")
print(filmes_set)  # {'Matrix Resurrections', 'Matrix Revolutions', 'Matrix'}

# Tentando remover um filme que não está no conjunto (gerará um erro)
filmes_set.remove("Avatar")  # KeyError: 'Avatar'

# Usando discard para remover um filme (não gera erro se o filme não estiver no conjunto)
filmes_set.discard("Avatar")  # Não gera erro, apenas não faz nada
print(filmes_set)  # {'Matrix Resurrections', 'Matrix Revolutions', 'Matrix'}

# Limpando o conjunto
filmes_set.clear()
print(filmes_set)  # set() (o conjunto está vazio)

# Verificando se o conjunto está vazio
print(len(filmes_set) == 0)  # True (o conjunto está vazio)

# Criando um conjunto vazio
filmes_vazio = set()
print(filmes_vazio)  # set() (o conjunto está vazio)

# Verificando se o conjunto é vazio
print(len(filmes_vazio) == 0)  # True (o conjunto está vazio)

# Criando um conjunto a partir de uma lista (converte duplicatas em valores únicos)
lista_filmes = ["Matrix", "Matrix Reloaded", "Matrix Revolutions", "Matrix"]
filmes_set_from_list = set(lista_filmes)
print(filmes_set_from_list)  # {'Matrix Reloaded', 'Matrix Revolutions', 'Matrix'}

# Verificando se dois conjuntos são iguais
conjunto1 = {"Matrix", "Matrix Reloaded"}
conjunto2 = {"Matrix Reloaded", "Matrix"}
print(conjunto1 == conjunto2)  # True (os conjuntos são iguais, pois a ordem não importa)

# Verificando se um conjunto é um subconjunto de outro
conjunto3 = {"Matrix"}
conjunto4 = {"Matrix", "Matrix Reloaded"}
print(conjunto3.issubset(conjunto4))  # True (conjunto3 é um subconjunto de conjunto4)

# Verificando se um conjunto é um superconjunto de outro
conjunto5 = {"Matrix", "Matrix Reloaded"}
conjunto6 = {"Matrix"}
print(conjunto5.issuperset(conjunto6))  # True (conjunto5 é um superconjunto de conjunto6)

# Realizando operações de união, interseção e diferença entre conjuntos
conjunto_a = {"Matrix", "Matrix Reloaded"}
conjunto_b = {"Matrix Reloaded", "Matrix Revolutions"}

# União (todos os elementos de ambos os conjuntos)
uniao = conjunto_a.union(conjunto_b)
print(uniao)  # {'Matrix Reloaded', 'Matrix Revolutions', 'Matrix'}

# Interseção (elementos comuns a ambos os conjuntos)
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)  # {'Matrix Reloaded'}

# Diferença (elementos que estão em conjunto_a, mas não em conjunto_b)
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)  # {'Matrix'} (elementos que estão em conjunto_a, mas não em conjunto_b)

# Diferença simétrica (elementos que estão em um dos conjuntos, mas não em ambos)
diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)  # {'Matrix', 'Matrix Revolutions'} (elementos que estão em um dos conjuntos, mas não em ambos)

# Verificando se dois conjuntos são disjuntos (não têm elementos em comum)
conjunto7 = {"Avatar"}
conjunto8 = {"Titanic"}
print(conjunto7.isdisjoint(conjunto8))  # True (os conjuntos não têm elementos em comum)
