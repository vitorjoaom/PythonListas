vetorA = [10]
vetorB = [10]
vetorC = [20]
aux1 = 0
aux2 = 0

for i in range(10):
    aux1 = float(input(f"Digite o valor {i+1} do vetor A: "))
    vetorA.append(aux1)
    aux2 = float(input(f"Digite o valor {i+1} do vetor B: "))
    vetorB.append(aux2)
vetorC = vetorA + vetorB
print(vetorC)    