# 1. Saudar o usuário e solicitar o input do nome
nome = input("Olá! Digite seu nome: ").strip()

salario = float(input(f"Bem-vindo, {nome}! Insira seu salario mensal: "))

bonus = float(input(f"{nome}, informe o valor do bônus: "))

total = (salario * bonus) + 1000

print(f"{nome}, seu bonus total no ano é: R$ {total}")