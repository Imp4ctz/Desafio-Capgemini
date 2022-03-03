import math
texto = input("Digite sua frase: ")
novoTexto = texto.replace(" ", "")
vetor = list(novoTexto)
raiz = math.sqrt(len(vetor))
tamanhoMatriz = round(raiz+0.5)
vetor2 = []
vetorAux = []
for x in range(len(novoTexto)):
    vetor2.append(vetor[x])
    if len(vetor2) == int(tamanhoMatriz):
        vetorAux.append(vetor2)
        vetor2 = []
i = len(vetor2)
while i < tamanhoMatriz:
    vetor2.append(" ")
    i = i+1
vetorAux.append(vetor2)
vetorAux2 = []
vetor = []
print(vetorAux)
for x in range(len(vetorAux)):
    for y in range(len(vetorAux[x])):
        vetor.append(vetorAux[y][x])
        if len(vetor) == int(tamanhoMatriz):
            vetorAux2.append(vetor)
            vetor = []
vetorAux2.append(vetor)

for x in range(len(vetorAux2)):
    print(vetorAux2[x])