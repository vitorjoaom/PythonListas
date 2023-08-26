vetor = [20]
vetorimpar = []
vetorpar = []

for i in range(20):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)
    if(valor%2 == 0):
        vetorpar.append(valor)
    else:
        vetorimpar.append(valor)    

print(f"A quantidade de numeros ímpares é: ")
print(vetorimpar) 
print(f"A quantidade de numeors pares é: ")
print(vetorpar)
print(f"A quantidade de números totais é: ")   
print(vetor)        