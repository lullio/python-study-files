# Programa principal

# Acessar o módulo math_operations (outro arquivo math_operations.py)
import math_operations # importa tudo do arquivo
from math_operations import multiply, divide # maneira de importar só algumas funções

print(math_operations.sum(5, 3))
print(math_operations.subtract(5, 3))

print(multiply(5, 3)) # chama diretamente a função, não precisa do math_operations
print(divide(5, 3)) # chama diretamente a função, não precisa do math_operations

import string_utils
print(string_utils.capitalize("hello"))
print(string_utils.reverse_string("python"))
print(string_utils.count("apple"))