vetor = []
qntNum = int(input("Informe a quantidade de números da lista "))
for x in range(qntNum):
    numero = int(input("Digite o Número "))
    vetor.append(numero)
num = int(input("Informe o número para o calculo "))
pares = 0
for x in range(len(vetor)):
    for y in range(len(vetor)):
        if vetor[x] + num == vetor[y]:
            pares = pares + 1
print(pares)
input("Press enter to exit")