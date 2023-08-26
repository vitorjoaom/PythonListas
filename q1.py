vetor = []

for i in range(5):
    valor = int(input(f"Digite o número {i+1}: "))
    vetor.append(valor)
    
print("\n")
for i in range(5):
    print(f"Elemento {i+1}: {vetor[i]}\n")    