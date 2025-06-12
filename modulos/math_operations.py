# Módulo de operações matemáticas
def sum(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y!= 0:
      return x / y
   else:
      raise ValueError("Não é permtido divisão por zero")
