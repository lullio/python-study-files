"""
Fatorial de um número usando função recursiva
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
4 -> 4 * 3 * 2 * 1
"""
# 10 - Função recursiva para calcular o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:  # Caso base: fatorial de 0 ou 1 é 1
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva para calcular o fatorial
number = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {number} é: {fatorial(number)}")  # Chama a função recursiva e imprime o resultado
"""
Por que não precisa de loop?
A recursão funciona como um loop implícito que vai "descendo" até o caso base. Cada chamada da função resolve uma parte do problema e depende do resultado da próxima chamada:

- A função chama a si mesma com n-1.

- Essa nova chamada chama a próxima com n-2.

- Isso continua até chegar em n == 1 (caso base).

Depois, as chamadas começam a retornar os valores e multiplicar, calculando o resultado final.

Assim, a função "repete" o cálculo de forma natural, sem precisar de um for ou while. O processo de "loop" acontece através das chamadas da função empilhadas na memória.

Exemplo rápido
Para calcular fatorial(3):

fatorial(3) retorna 3 * fatorial(2)
fatorial(2) retorna 2 * fatorial(1)
fatorial(1) retorna 1 (caso base)

Agora as chamadas vão retornando:
fatorial(2) = 2 * 1 = 2
fatorial(3) = 3 * 2 = 6   
"""

# 2 - Soma total de um número de elementos usando função recursiva
def soma_total(n):
    if n == 0:  # Caso base: soma de 0 elementos é 0
        return 0
    else:
        return n + soma_total(n - 1)  # Chamada recursiva para somar os números até n
number = int(input("Digite um número para calcular a soma total: "))
print(f"A soma total de 1 até {number} é: {soma_total(number)}")  # Chama a função recursiva e imprime o resultado
"""Por que não precisa de loop?
A recursão funciona como um loop implícito que vai "descendo" até o caso base. Cada chamada da função resolve uma parte do problema e depende do resultado da próxima chamada:
- A função chama a si mesma com n-1.
- Essa nova chamada chama a próxima com n-2.
- Isso continua até chegar em n == 0 (caso base).
Depois, as chamadas começam a retornar os valores e somar, calculando o resultado final.
Assim, a função "repete" o cálculo de forma natural, sem precisar de um for ou while. O processo de "loop" acontece através das chamadas da função empilhadas na memória.
Exemplo rápido
Para calcular soma_total(3):
soma_total(3) retorna 3 + soma_total(2)
soma_total(2) retorna 2 + soma_total(1)
soma_total(1) retorna 1 + soma_total(0)
soma_total(0) retorna 0 (caso base)
Agora as chamadas vão retornando:
soma_total(1) = 1 + 0 = 1
soma_total(2) = 2 + 1 = 3
soma_total(3) = 3 + 3 = 6
"""
 