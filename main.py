import sys

# Closure para gerar IDs automaticamente
def gerador_id_tarefa():
    contador_id = 0
    def proximo_id():
        nonlocal contador_id
        contador_id += 1
        return contador_id
    return proximo_id

gerar_id = gerador_id_tarefa()

# Lista de tarefas
tarefas = []

# Função para gerar um ID único
def gerar_id():
    return len(tarefas) + 1

# Adicionar nova tarefa
def adicionar_tarefa(descricao, prioridade=1):
    try:
        prioridade = int(prioridade)
    except ValueError:
        print("Erro: A prioridade deve ser um número inteiro.")
        return
    
    tarefas.append({
        "id": gerar_id(),
        "descricao": descricao,
        "prioridade": prioridade,
        "concluida": False
    })
    
    print(f"Tarefa adicionada: '{descricao}' com prioridade {prioridade}")

# Remover tarefa pelo ID
def remover_tarefa(id_tarefa):
    global tarefas
    
    # Encontra a tarefa antes de removê-la
    tarefa_removida = next((tarefa for tarefa in tarefas if tarefa["id"] == id_tarefa), None)
    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != id_tarefa]  # Remove a tarefa
    
    if tarefa_removida:
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso.")
    else:
        print(f"Nenhuma tarefa encontrada com o ID {id_tarefa}.")
    
    return tarefas

