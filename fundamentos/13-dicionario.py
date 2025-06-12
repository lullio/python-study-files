# Dicionário em Python
# Um dicionário é uma coleção de pares chave-valor, onde cada chave é única e mapeada para um valor. 
# Dicionários são mutáveis, o que significa que você pode adicionar, remover e modificar pares chave-valor após a criação do dicionário.
# É parecido com o JSON do JavaScript, onde você tem chaves e valores associados.


# Criando um dicionário do fime Matrix
filme_matrix = {
    "nome": "Matrix",
    "ano_lancamento": 1999,
    "avaliacao": 8.7,
    "genero": ["Ficção Científica", "Ação"],
    "diretores": ["Lana Wachowski", "Lilly Wachowski"],
      "elenco": [
         {"ator": "Keanu Reeves", "personagem": "Neo"},
         {"ator": "Laurence Fishburne", "personagem": "Morpheus"},
         {"ator": "Carrie-Anne Moss", "personagem": "Trinity"}
      ]
}
# Verificando o tipo de dado do dicionário
print(type(filme_matrix))  # <class 'dict'>
# Verificando se o dicionário é vazio
print(len(filme_matrix) == 0)  # False (o dicionário não está vazio)
# Verificando o tamanho do dicionário
print(len(filme_matrix))  # 7 (o dicionário tem 7 pares chave-valor)
# Verificando se o dicionário é mutável
print(isinstance(filme_matrix, dict))  # True (dicionários são mutáveis)


# 1. Acessando valores do dicionário
print(filme_matrix["nome"])  # Matrix
print(filme_matrix.get("nome"))  # Matrix

print(filme_matrix["ano_lancamento"])  # 1999
print(filme_matrix["avaliacao"])  # 8.7
print(filme_matrix["genero"])  # ['Ficção Científica', 'Ação']
print(filme_matrix["diretores"])  # ['Lana Wachowski', 'Lilly Wachowski']

# 2. Buscando apenas as chaves do dicionário
print(filme_matrix.keys()) # dict_keys(['nome', 'ano_lancamento', 'avaliacao', 'genero', 'diretores', 'elenco'])

# 3. Buscando apenas os valores do dicionário
print(filme_matrix.values())  # dict_values(['Matrix', 1999, 8.7, ['Ficção Científica', 'Ação'], ['Lana Wachowski', 'Lilly Wachowski'], [{'ator': 'Keanu Reeves', 'personagem': 'Neo'}, {'ator': 'Laurence Fishburne', 'personagem': 'Morpheus'}, {'ator': 'Carrie-Anne Moss', 'personagem': 'Trinity'}]])

# 4. Buscando os itens do dicionário (pares chave-valor). Ele exibe uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente.
print(filme_matrix.items())  # dict_items([('nome', 'Matrix'), ('ano_lancamento', 1999), ('avaliacao', 8.7), ('genero', ['Ficção Científica', 'Ação']), ('diretores', ['Lana Wachowski', 'Lilly Wachowski']), ('elenco', [{'ator': 'Keanu Reeves', 'personagem': 'Neo'}, {'ator': 'Laurence Fishburne', 'personagem': 'Morpheus'}, {'ator': 'Carrie-Anne Moss', 'personagem': 'Trinity'}])])

# 5. Adicionando um novo par chave-valor ao dicionário
filme_matrix["duracao"] = 136  # Adiciona a duração do filme
print(filme_matrix["duracao"])  # 136
filme_matrix["produtores"] = ["Joel Silver", "Lana Wachowski", "Lilly Wachowski"]  

# 6. Atualizando um valor existente no dicionário
filme_matrix["avaliacao"] = 9.0  # Atualiza a avaliação do filme
print(filme_matrix["avaliacao"])  # 9.0
# Ou usando update
filme_matrix.update({"avaliacao": 9.0})  # Atualiza a avaliação do filme

# 7. Verificando se uma chave existe no dicionário
print("nome" in filme_matrix)  # True (a chave "nome" existe)
print("produtores" in filme_matrix)  # False (a chave "produtores" não existe)

# 8. Verificando se um valor está presente no dicionário
print("Matrix" in filme_matrix.values())  # True (o valor "Matrix" está presente)   
print("Avatar" in filme_matrix.values())  # False (o valor "Avatar" não está presente)

# 9. Removendo um par chave-valor do dicionário
filme_matrix.pop("duracao")  # Remove a chave "duracao" e seu valor
print(filme_matrix)  # {'nome': 'Matrix', 'ano_lancamento': 1999, 'avaliacao': 9.0, 'genero': ['Ficção Científica', 'Ação'], 'diretores': ['Lana Wachowski', 'Lilly Wachowski'], 'elenco': [{'ator': 'Keanu Reeves', 'personagem': 'Neo'}, {'ator': 'Laurence Fishburne', 'personagem': 'Morpheus'}, {'ator': 'Carrie-Anne Moss', 'personagem': 'Trinity'}], 'produtores': ['Joel Silver', 'Lana Wachowski', 'Lilly Wachowski']}

# 10. Limpando o dicionário
filme_matrix.clear()  # Limpa todos os pares chave-valor do dicionário
print(filme_matrix)  # {} (o dicionário está vazio)