# 8. Escreva um algoritmo para ler dois números e apresente
# a multiplicação deles apenas se o resultado for maior ou igual a 50. 

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 >= 50:
    mult = num1 * num2
    print("A multiplicação dos números é: ",mult)

print("Programa encerrado")
