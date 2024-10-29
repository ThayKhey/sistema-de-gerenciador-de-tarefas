# Dicionário de Projetos e Tarefas

Este projeto implementa um dicionário simples para armazenar projetos e suas respectivas tarefas. É uma ferramenta útil para gerenciar atividades e garantir que todos os passos de um projeto sejam acompanhados.

## Funcionalidades

### 1. Adicionar um Novo Projeto
Permite ao usuário criar um novo projeto, que será armazenado no dicionário. Caso o projeto já exista, uma mensagem de aviso será exibida.

**Exemplo:**
```python
adicionar_projeto("Projeto Alpha")
```

### 2. Adicionar uma Tarefa a um Projeto
Permite a adição de uma nova tarefa a um projeto existente. Cada tarefa inclui título, descrição, responsável e status.

**Exemplo:**
```python
adicionar_tarefa("Projeto Alpha", "Tarefa 1", "Descrição da Tarefa 1", "João")
```

### 3. Atualizar o Status de uma Tarefa
Possibilita a atualização do status de uma tarefa específica dentro de um projeto.

**Exemplo:**
```python
atualizar_tarefa("Projeto Alpha", "Tarefa 1", "em andamento")
```

### 4. Listar Tarefas de um Projeto
Exibe todas as tarefas associadas a um projeto, com detalhes sobre título, descrição, responsável e status.

**Exemplo:**
```python
listar_tarefas("Projeto Alpha")
```

## Estrutura do Código

- **Dicionário `projetos`:** Armazena os projetos e suas tarefas.
- **Funções:**
  - `adicionar_projeto(nome_projeto)`: Adiciona um novo projeto.
  - `adicionar_tarefa(nome_projeto, titulo, descricao, responsavel, status)`: Adiciona uma tarefa a um projeto.
  - `atualizar_tarefa(nome_projeto, titulo, novo_status)`: Atualiza o status de uma tarefa.
  - `listar_tarefas(nome_projeto)`: Lista todas as tarefas de um projeto.

## Como Usar

1. Importe ou copie o código para o seu ambiente Python.
2. Utilize as funções conforme a necessidade para gerenciar seus projetos e tarefas.

## Contribuições

Sinta-se à vontade para contribuir com melhorias e novas funcionalidades! Suas sugestões são bem-vindas.

## Licença

Este projeto é de uso livre. Você pode modificá-lo e distribuí-lo como desejar.
