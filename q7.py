num_elementos = 10
vetor = [0] * num_elementos 
multiplicacao = 1
soma = 0

for i in range(5):
    vetor[i] = int(input(f"Digite o número {i+1}: "))
    multiplicacao = multiplicacao * vetor[i]
    soma = soma + vetor[i]    
      
print(vetor)
print(multiplicacao)
print(soma)    