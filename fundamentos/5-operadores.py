num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"Potência de {num1} elevado a {num2} é: {num1 ** num2}")
print(f"O resto da divisão de {num1} por {num2} é: {num1 % num2}")
print(f"Comparando se num1 maior que num2: {num1 > num2}")

# Aritmetic Operators
print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")
print(f"Divisão inteira: {num1 // num2}")
print(f"Módulo: {num1 % num2}") # resto da divisão
print(f"Exponenciação: {num1 ** num2}")


# Comparison Operators
print(f"É igual? {num1 == num2}")
print(f"É diferente? {num1 != num2}")
print(f"É maior? {num1 > num2}")
print(f"É menor? {num1 < num2}")
print(f"É maior ou igual? {num1 >= num2}")
print(f"É menor ou igual? {num1 <= num2}")


# Logical Operators
print(f"AND: {num1 > 0 and num2 > 0}")
print(f"OR: {num1 > 0 or num2 > 0}")
print(f"NOT: {not (num1 > 0)}")


# Assignment Operators / Atribuição
num1 += 5  # num1 = num1 + 5
print(f"num1 após += 5: {num1}")
num2 *= 2  # num2 = num2 * 2
print(f"num2 após *= 2: {num2}")
num1 -= 3  # num1 = num1 - 3
print(f"num1 após -= 3: {num1}")
num2 /= 4  # num2 = num2 / 4
print(f"num2 após /= 4: {num2}")


# Identity Operators
print(f"num1 é num2? {num1 is num2}")
print(f"num1 é diferente de num2? {num1 is not num2}")


# Membership Operators
lista = [1, 2, 3, 4, 5]
print(f"1 está na lista? {1 in lista}")
print(f"6 está na lista? {6 not in lista}")


# Bitwise Operators
print(f"AND bitwise: {num1 & num2}")
print(f"OR bitwise: {num1 | num2}")
print(f"XOR bitwise: {num1 ^ num2}")
print(f"NOT bitwise: {~num1}")
print(f"Deslocamento à esquerda: {num1 << 1}")
print(f"Deslocamento à direita: {num1 >> 1}")


# Ternary Operator
print(f"Maior número: {num1 if num1 > num2 else num2}")
