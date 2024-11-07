from pyDatalog import pyDatalog

# Criando os termos
pyDatalog.create_terms('Colaborador, Projeto, Nome, Idade, Departamento, colaborador, projeto')

# Função para carregar os dados dos arquivos
def carregar_dados():
    # Importando colaboradores
    with open("colaboradores.txt", "r") as file:
        for line in file:
            nome, idade, departamento = line.strip().split(',')
            +Colaborador(nome)

    # Importando projetos
    with open("projetos.txt", "r") as file:
        for line in file:
            nome_projeto, departamento = line.strip().split(',')
            +Projeto(nome_projeto)

# Carregar os dados
carregar_dados()

# Consultas para exibir os nomes dos colaboradores e projetos
print("Lista de Colaboradores:")
print(Colaborador(Nome))

print("\nLista de Projetos:")
print(Projeto(Nome))
