# Comandos de decisão - if

idade = int(input("Digite sua idade: "))
if idade > 18:
    print ("Maior de idade")


aluno = str(input("É aluno Etec? [s/n]: "))
if aluno == 's':
    print("Bem-vindo aluno")
elif aluno == 'n':
    print("Bem-vindo convidado\n")
else:
    print("Opção inválida")

print ("Programa encerrado")