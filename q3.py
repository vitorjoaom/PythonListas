vetor = []
media = 0

for i in range(4):
    valor = int(input(f"Digite o número {i+1}: "))
    vetor.append(valor)
    media += valor

print(f"A media dos valores é: {media/4}")