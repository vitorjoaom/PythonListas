vetor = []

for i in range(10):
    valor = int(input(f"Digite o número {i+1}: "))
    vetor.append(valor)
    
vetor.sort(reverse = True)
print(vetor)