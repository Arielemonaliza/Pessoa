soma = 0
n = 3
for i in range(1, n + 1):
    numero = float(input(f"digite o {1}° número:" ))
    soma += numero
    multiplicacao = soma / n
    print("A média dos numeros digitados é:", multiplicacao)