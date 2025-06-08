# Informações sobre o filme:

name = input("Digite o nome do filme: ")
year_launch = int(input("Digite o ano de lançamento: "))
rating = float(input("Digite a avaliação do filme: "))
plan_included = input("O filme está incluído no plano? (s/n): ").lower() == 's'

# Exibindo as informações do filme
print(f"Nome do filme: {name}")
print(f"Ano de lançamento: {year_launch}")
print(f"Avaliação: {rating}")
print(f"Está incluído no plano: {'Sim' if plan_included else 'Não'}")

# Verificando se o filme é recomendado
if rating >= 8.0:
   print(f"O filme {name} é muito bom, tem avaliação {rating}")
else:
   print("O filme {name} não tem uma boa avalição: {rating}")