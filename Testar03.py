from pyDatalog import pyDatalog

# Criando os termos
pyDatalog.create_terms('Colaborador, Projeto, ParticipaDe, DepartamentoColaborador, Senior, NomeColaborador, NomeProjeto, NomeDepartamento, Nome, Idade, Departamento, count')

# Função para carregar os dados dos arquivos
def carregar_dados():
    # Importando colaboradores e associando ao departamento
    with open("colaboradores.txt", "r") as file:
        for line in file:
            nome, idade, departamento = line.strip().split(',')
            idade = int(idade)
            +Colaborador(nome)
            +DepartamentoColaborador(nome, departamento)
            if idade > 30:
                +Senior(nome)  # Definindo como Senior caso idade > 30

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

# Listar todos os colaboradores sêniores e o departamento ao qual pertencem
print("Colaboradores Sêniores e seus Departamentos:")
query = (Senior(NomeColaborador) & DepartamentoColaborador(NomeColaborador, NomeDepartamento))
for row in query.data:
    print(f"Colaborador Sênior: {row[0]}, Departamento: {row[1]}")

# Contar o número de colaboradores sêniores em cada departamento
print("\nContagem de Colaboradores Sêniores por Departamento:")
pyDatalog.create_terms('D, C')
query_count = (DepartamentoColaborador(NomeColaborador, D) & Senior(NomeColaborador)) <= count(D, C)
for row in query_count.data:
    print(f"Departamento: {row[0]}, Número de Colaboradores Sêniores: {row[1]}")
