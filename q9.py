vetor1 = []
valor = 0
quadrado = 0

for i in range(5):
    valor = int(input(f"Digite o valor do valor número {i+1}: "))
    vetor1.append(valor)
    quadrado += valor * valor       
    
print(quadrado)    