idade = [5]
altura = [5]
valor1 = 0
valor2 = 0

for i in range(5):
    valor1 = int(input(f"Digite a altura da pessoa número {i+1}: "))
    altura.append(valor1)
    valor2 = int(input(f"Digite a idade da pessoa {i+1}: "))
    idade.append(valor2)
    
idade.sort(reverse = True)
altura.sort(reverse = True)
print(idade)
print(altura)
