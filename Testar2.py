from pyDatalog import pyDatalog

# Criando os termos
pyDatalog.create_terms('Colaborador, Projeto, ParticipaDe, DepartamentoColaborador, NomeColaborador, NomeProjeto, NomeDepartamento, Nome, Idade, Departamento')

# Função para carregar os dados dos arquivos
def carregar_dados():
    # Importando colaboradores e associando ao departamento
    with open("colaboradores.txt", "r") as file:
        for line in file:
            nome, idade, departamento = line.strip().split(',')
            +Colaborador(nome)
            +DepartamentoColaborador(nome, departamento)

    # Importando projetos
    with open("projetos.txt", "r") as file:
        for line in file:
            nome_projeto, departamento = line.strip().split(',')
            +Projeto(nome_projeto)

    # Importando alocações para definir quem participa de qual projeto
    with open("alocacoes.txt", "r") as file:
        for line in file:
            nome_colaborador, nome_projeto = line.strip().split(',')
            +ParticipaDe(nome_colaborador, nome_projeto)

# Carregar os dados
carregar_dados()

# Listar todos os colaboradores, seus projetos e departamentos
print("Colaboradores, Projetos e Departamentos:")
query = (ParticipaDe(NomeColaborador, NomeProjeto) & DepartamentoColaborador(NomeColaborador, NomeDepartamento))
for row in query.data:
    print(f"Colaborador: {row[0]}, Projeto: {row[1]}, Departamento: {row[2]}")
