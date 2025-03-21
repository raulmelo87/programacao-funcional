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

