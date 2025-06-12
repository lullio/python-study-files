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
   print(f"O filme {name} não tem uma boa avalição: {rating}")

   

num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
operation = input("Digite a operação a ser realizada: (+ * /)\n")

if operation == "+":
   print(f"A soma dos números é igual a {num1 + num2}")
elif operation == "*":
   print(f"A multiplicação dos números é igual a {num1 * num2}")
elif operation == "/":
   print(f"A divisão dos números é igual a {num1 / num2}:.2f") # .2f = duas casas decimais
else:
   print("Operação inválida")
