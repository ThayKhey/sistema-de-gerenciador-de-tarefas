''' Dicionário para armazenar os projetos e suas tarefas'''
projetos = {}

# Função para adicionar um novo projeto
def adicionar_projeto(nome_projeto):
    if nome_projeto not in projetos:
        projetos[nome_projeto] = []
        print(f"Projeto '{nome_projeto}' adicionado com sucesso.")
    else:
        print(f"O projeto '{nome_projeto}' já existe.")
 
# Função para adicionar uma nova tarefa a um projeto
def adicionar_tarefa(nome_projeto, titulo, descricao, responsavel, status="não iniciado"):
    if nome_projeto in projetos:
        tarefa = {
            "título": titulo,
            "descrição": descricao,
            "responsável": responsavel,
            "status": status
        }
        projetos[nome_projeto].append(tarefa)
        print(f"Tarefa '{titulo}' adicionada ao projeto '{nome_projeto}'.")
    else:
        print(f"O projeto '{nome_projeto}' não existe.")
 
# Função para atualizar o status de uma tarefa específica
def atualizar_tarefa(nome_projeto, titulo, novo_status):
    if nome_projeto in projetos:
        for tarefa in projetos[nome_projeto]:
            if tarefa["título"] == titulo:
                tarefa["status"] = novo_status
                print(f"Status da tarefa '{titulo}' atualizado para '{novo_status}'.")
                return
        print(f"Tarefa '{titulo}' não encontrada no projeto '{nome_projeto}'.")
    else:
        print(f"O projeto '{nome_projeto}' não existe.")
 
# Função para listar todas as tarefas de um projeto
def listar_tarefas(nome_projeto):
    if nome_projeto in projetos:
        if projetos[nome_projeto]:
            print(f"Tarefas do projeto '{nome_projeto}':")
            for tarefa in projetos[nome_projeto]:
                print(f"- Título: {tarefa['título']}, Descrição: {tarefa['descrição']}, "
                      f"Responsável: {tarefa['responsável']}, Status: {tarefa['status']}")
        else:
            print(f"O projeto '{nome_projeto}' não possui tarefas.")
    else:
        print(f"O projeto '{nome_projeto}' não existe.")
