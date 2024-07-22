n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = n1 + n2
if (n1 % 1 == 0):
    n1 = int(n1)
if (n2 % 1 == 0):
    n2 = int(n2)
if (n3 % 2 == 0):
    print(f"A soma de {n1} + {n2} é igual a {n3}. {n3} é um número par")
else:
    print(f"A soma de {n1} + {n2} é igual a {n3}. {n3} é um número impar")