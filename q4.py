vetor = [10]
cont = 0

for i in range(10):
    valor = str(input(f"Digite a letra {i+1}: "))
    vetor.append(valor)
    if(valor =='A' or valor =='E' or valor =='I' or valor =='O' or valor =='U'):
        cont += 1

print(f"A quantidade de vogais é: {10-cont}")    
        