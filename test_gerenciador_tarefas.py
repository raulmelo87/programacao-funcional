import unittest

# Reutilizando as funções
from main import adicionar_tarefa, remover_tarefa, listar_tarefas,
concluir_tarefa, listar_tarefas_pendentes, gerar_id, tarefas

class TestGerenciadorDeTarefas(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    """Método que é chamado uma vez antes de todos os testes"""
    cls.tarefas = tarefas
    cls.gerar_id = gerar_id
    
  def setUp(self):
    global tarefas
    tarefas.clear()
  
  def test_adicionar_tarefa(self):
    """Teste de adicionar uma tarefa"""
      adicionar_tarefa("Estudar Python", 2)
      self.assertEqual(len(self.tarefas), 1)
      self.assertEqual(self.tarefas[0]["descricao"], "Estudar Python")
      self.assertEqual(self.tarefas[0]["prioridade"], 2)
    
  def test_remover_tarefa(self):
    """Teste de remover uma tarefa"""
    global tarefas
    
    adicionar_tarefa("Estudar Python", 2)
    id_tarefa = tarefas[0]["id"]
    tarefas = remover_tarefa(id_tarefa)
    
    self.assertEqual(len(tarefas), 0)
    
  def test_remover_tarefa_inexistente(self):
    """Teste de remover uma tarefa que não existe"""
    id_tarefa_invalido = 9999
    lista = listar_tarefas()
    resultado = remover_tarefa(id_tarefa_invalido)
    self.assertEqual(len(resultado), len(resultado))
    
  def test_concluir_tarefa(self):
    """Teste de concluir uma tarefa"""
    adicionar_tarefa("Estudar Python", 2)
    id_tarefa = self.tarefas[0]["id"]
    concluir_tarefa(id_tarefa)
    self.assertTrue(self.tarefas[0]["concluida"])
    
  def test_listar_tarefas(self):
    """Teste de listar tarefas"""
    adicionar_tarefa("Estudar Python", 2)
    adicionar_tarefa("Estudar Matemática", 1)
    
    tarefas_listadas = listar_tarefas()
    
    self.assertEqual(len(tarefas_listadas), 2)
    self.assertEqual(tarefas_listadas[0]["descricao"], "Estudar Python")
    
  def test_listar_tarefas_pendentes(self):
    """Teste de listar apenas tarefas pendentes"""
    adicionar_tarefa("Estudar Python", 2)
    adicionar_tarefa("Estudar Matemática", 1)
    concluir_tarefa(self.tarefas[0]["id"])
    tarefas_pendentes = listar_tarefas_pendentes()
    self.assertEqual(len(tarefas_pendentes), 1)
    self.assertEqual(tarefas_pendentes[0]["descricao"], "Estudar Matemática")
    
if __name__ == "__main__":
unittest.main()
