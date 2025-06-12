import pprint

# Criando um dicionário de filmes
filmes_dict = {
    "Matrix": {
        "ano_lancamento": 1999,
        "avaliacao": 8.7,
        "genero": "Ficção Científica",
        "diretores": ["Lana Wachowski", "Lilly Wachowski"]
    },
    "Matrix Reloaded": {
        "ano_lancamento": 2003,
        "avaliacao": 7.2,
        "genero": "Ficção Científica",
         "diretores": ["Lana Wachowski", "Lilly Wachowski"]
    },
    "Matrix Revolutions": {
        "ano_lancamento": 2003,
        "avaliacao": 6.8,
        "genero": "Ficção Científica",
        "diretores": ["Lana Wachowski", "Lilly Wachowski"]
    }
}

print(filmes_dict)  # Exibe o dicionário de filmes, não fica legível no terminal

# Usando pprint para exibir o dicionário de forma legível
pp = pprint.PrettyPrinter(indent=4) # PrettyPrinter com indentação de 4 espaços
pp.pprint(filmes_dict)  # Exibe o dicionário de forma legível

# 1 - Acessando um filme específico
print(filmes_dict["Matrix"])  # Acessa o dicionário do filme "Matrix"

print(filmes_dict["Matrix"]["ano_lancamento"])  # Acessa o ano de lançamento do filme "Matrix"
print(filmes_dict["Matrix"]["avaliacao"])  # Acessa a avaliação do filme "Matrix"

# 2 - Adicionando um novo filme ao dicionário
filmes_dict["Matrix Resurrections"] = {
    "ano_lancamento": 2021,
    "avaliacao": 5.7,
    "genero": "Ficção Científica",
    "diretores": ["Lana Wachowski"]
}

# 3 - Adicionar novo item ao filme existente
filmes_dict["Matrix"]["elenco"] = [
    {"ator": "Keanu Reeves", "personagem": "Neo"}, 
    {"ator": "Laurence Fishburne", "personagem": "Morpheus"},
    {"ator": "Carrie-Anne Moss", "personagem": "Trinity"}
]

# 4 - Excluindo um filme do dicionário
del filmes_dict["Matrix Revolutions"]  # Remove o filme "Matrix Revolutions"
pp.pprint(filmes_dict)  # Exibe o dicionário atualizado

# 5 - Verificando se um filme existe no dicionário
print("Matrix" in filmes_dict)  # True (o filme "Matrix" existe)  
print("Avatar" in filmes_dict)  # False (o filme "Avatar" não existe)

# 6 - Verificando se um filme tem um determinado diretor
print("Lana Wachowski" in filmes_dict["Matrix"]["diretores"])  # True (Lana Wachowski é diretora de "Matrix")
print("James Cameron" in filmes_dict["Matrix"]["diretores"])  # False (James Cameron não é diretor de "Matrix")

# 7 - Atualizando a avaliação de um filme
filmes_dict["Matrix"]["avaliacao"] = 9.0  # Atualiza a avaliação do filme "Matrix"

# 8 - Exibindo todos os filmes e suas informações
for filme, detalhes in filmes_dict.items():
    print(f"Filme: {filme}")
    print(f"Ano de Lançamento: {detalhes['ano_lancamento']}")
    print(f"Avaliação: {detalhes['avaliacao']}")
    print(f"Gênero: {detalhes['genero']}")
    print(f"Diretores: {', '.join(detalhes['diretores'])}")
    if "elenco" in detalhes:
        elenco = ", ".join([f"{ator['ator']} como {ator['personagem']}" for ator in detalhes["elenco"]])
        print(f"Elenco: {elenco}")
    print()  # Linha em branco para separar os filmes
    
# 9 - Limpando o dicionário de filmes
filmes_dict.clear()  # Limpa todos os filmes do dicionário