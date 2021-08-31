# Laço de repetição - While
# Contadores e acumuladores

cont = 1
acumulador = 0
num = int(input("Digite um número máximo: "))
while cont <= num:
    print(cont)
    acumulador = acumulador + cont
    #cont = cont + 1
    cont += 1
print("Soma total dos números é",acumulador)