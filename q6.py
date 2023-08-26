# Número de alunos
num_alunos = 10

medias_alunos = []

for i in range(num_alunos):
    notas = []  
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)   
    
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

num_alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: {num_alunos_aprovados}")