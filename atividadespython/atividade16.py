#faca um algoritmo que receba o peso de uma pessoa
# Dados
peso = float(input("Informe o peso da pessoa (em kg): "))
# Cálculo do novo peso com engorda e emagrecimento
peso_engordar = peso * 1.15
peso_emagrecer = peso * 0.80
# Resultados do codigo
print("Novo peso se engordar 15%:", peso_engordar, "kg")
print("Novo peso se emagrecer 20%:", peso_emagrecer, "kg")