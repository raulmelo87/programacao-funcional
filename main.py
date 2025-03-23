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

# Listar tarefas (ordenadas por prioridade usando lambda)
def listar_tarefas():

    tarefas_ordenadas = sorted(tarefas, key=lambda t: t["prioridade"], reverse=True)
    if tarefas_ordenadas:
        for tarefa in tarefas_ordenadas:
            status = "✔" if tarefa["concluida"] else " "
            print(f"{tarefa['id']}: [{status}] {tarefa['descricao']} (Prioridade: {tarefa['prioridade']})")
    else:
        print('Lista de tarefas vazia.')
    
    return tarefas_ordenadas

# Marcar uma tarefa como concluída
def concluir_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["concluida"] = True

# Listar apenas tarefas pendentes usando list comprehension
def listar_tarefas_pendentes():
    pendentes = [t for t in tarefas if not t["concluida"]]
    for tarefa in pendentes:
        print(f"{tarefa['id']}: {tarefa['descricao']} (Prioridade: {tarefa['prioridade']})")
    
    return pendentes

# Função de alta ordem para aplicar ações em massa
def aplicar_em_todas_tarefas(acao):
    global tarefas
    tarefas = [acao(tarefa) for tarefa in tarefas]

# Exemplo de uso: marcar todas as tarefas como concluídas
def concluir_todas_tarefas():
    aplicar_em_todas_tarefas(lambda tarefa: {**tarefa, "concluida": True})

# Interface CLI
def cli():
    print("\nGerenciador de Tarefas - CLI")
    while True:
        comando = input("\nComandos: adicionar <desc> <prioridade>, remover <id>, listar, concluir <id>, pendentes, concluir_todas, sair\n> ").split()
        if not comando:
            continue
        
        acao = comando[0]

        if acao == "adicionar":
            if len(comando) > 1:
                # Verifica se a última palavra é um número (prioridade), se for, usa como prioridade
                if comando[-1].isdigit():
                    descricao = " ".join(comando[1:-1])  # Junta as palavras de 1 até o penúltimo item
                    prioridade = comando[-1]  # A última palavra é a prioridade
                else:
                    descricao = " ".join(comando[1:])  # Junta todas as palavras após o 'adicionar' como descrição
                    prioridade = "1"  # Prioridade padrão 1
                adicionar_tarefa(descricao, prioridade)
            else:
                print("Uso correto: adicionar <descrição> <prioridade (opcional)>")

        elif acao == "remover":
            if len(comando) > 1 and comando[1].isdigit():
                remover_tarefa(int(comando[1]))
            else:
                print("Uso correto: remover <id>")

        elif acao == "listar":
            listar_tarefas()

        elif acao == "concluir":
            if len(comando) > 1 and comando[1].isdigit():
                concluir_tarefa(int(comando[1]))
                print(f"Tarefa {comando[1]} concluída.")
            else:
                print("Uso correto: concluir <id>")

        elif acao == "pendentes":
            listar_tarefas_pendentes()

        elif acao == "concluir_todas":
            concluir_todas_tarefas()
            print("Todas as tarefas foram concluídas.")

        elif acao == "sair":
            print("Saindo...")
            sys.exit()

        else:
            print("Comando inválido! Use um dos seguintes: adicionar, remover, listar, concluir, pendentes, concluir_todas, sair.")

if __name__ == "__main__":
    cli()
