class Aluno:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero
        self.notas = {
            'Chico Bento': 0,
            'Magali': 0,
            'Monica': 0,
            'Cebolinha': 0
        }
    
    def inserir_notas(self, chico_bento, magali, monica, cebolinha):
        self.notas['Chico Bento'] = chico_bento
        self.notas['Magali'] = magali
        self.notas['Monica'] = monica
        self.notas['Cebolinha'] = cebolinha
    
    def media_notas(self):
        total_notas = len(self.notas)
        return sum(self.notas.values()) / total_notas
    
    def __str__(self):
        return f"{self.nome} ({'Mister' '👨‍🌾' if self.genero == '👩‍🌾' else 'Miss'})"


class Jurado:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome


# Criando os objetos Aluno
alunos = [
    Aluno('Beatriz', 'F'),
    Aluno('Mateus', 'M'),
    Aluno('Bruno Arantes', 'M'),
    Aluno('Bruno Oliveira', 'M'),
    Aluno('Daniela', 'F'),
    Aluno('Stefany', 'F')
]

# Criando os objetos Jurado
jurados = [
    Jurado('Chico Bento'),
    Jurado('Magali'),
    Jurado('Monica'),
    Jurado('Cebolinha')
]

# Função para inserir as notas de um aluno
def inserir_notas_aluno(aluno, notas):
    aluno.inserir_notas(*notas)

# Função para mostrar as notas de cada jurado
def mostrar_notas_jurado(jurado):
    for aluno in alunos:
        print(f"Nota de {jurado}: {aluno.notas[jurado.nome]}")

# Inserindo notas fictícias para cada aluno
notas_alunos = [
    (2.5, 2.5, 2.5, 2.5),  # Beatriz
    (2.5, 2.5, 2.5, 2.5),  # Mateus
    (2.5, 2.5, 2.5, 2.5),  # Bruno Arantes
    (2.5, 2.5, 2.5, 2.5),  # Bruno Oliveira
    (2.5, 2.5, 2.5, 2.5),  # Daniela
    (2.5, 2.5, 2.5, 2.5)   # Stefany
]

for aluno, notas in zip(alunos, notas_alunos): # o comando zip combina elementos de multiplas tuplas em listas 
    inserir_notas_aluno(aluno, notas)

# Exibindo notas dos jurado da quadrilha 
for jurado in jurados:
    print(f"\nNotas de {jurado}:")
    mostrar_notas_jurado(jurado)
    print()

# Exibindo a média das notas de cada aluno
for aluno in alunos:
    print(f"Média das notas de {aluno.nome}: {aluno.media_notas():.2f}")

# Exibindo gênero de um aluno específico (exemplo)
nome_aluno_input = input("\nDigite o nome de seu aluno ou aluna preferida: ")
for aluno in alunos:
    if aluno.nome.lower() == nome_aluno_input.lower():
        print(f"{aluno}: {aluno.genero}")
        break
else:
    print(f"Este aluno inserido'{nome_aluno_input}' concurso, entre somente com os valores, Beatriz, Mateus, Bruno Arantes, Bruno Oliveira, Daniela, Stefany")
