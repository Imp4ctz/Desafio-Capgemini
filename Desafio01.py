tamanhoVetor = int(input("Quantos números você quer colocar? "))
vetor = []
if tamanhoVetor % 2 == 0:
        tamanhoVetor = tamanhoVetor + 1
for x in range(tamanhoVetor):
    numero = int(input("Digite o Número "))
    vetor.append(numero)
vetor.sort()
print(vetor[int((len(vetor) / 2) - 0.5)])
input("Press enter to exit")