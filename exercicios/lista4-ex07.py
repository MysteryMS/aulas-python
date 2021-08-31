# 7. Escreva um algoritmo que leia 2 notas de um aluno e calcule a
# média final deste aluno, considerando que a média é ponderada, ou seja,
# o peso das notas são 3 e 7. 

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 * 0.3) + ( nota2 * 0.7)

print("A média ponderada é: ",media)
