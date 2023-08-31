from MockDB import MockBD
import sys
sys.path.insert(0, '..')
from conexaoDB import *
from prova_queries import *

#● Testes com Banco de Dados
#1. Encontrar a maior média já vista em uma turma de código TAD0203
#2. Listar todas as turmas (nome) e a média final (media) cursadas por um aluno (por exemplo, 'Carla')
#4. Listar o nome das turmas que tiveram alunos que tiraram média maior ou igual a 9,0.

class TestDB(MockBD):
    # 4. Listar o nome das turmas que tiveram alunos que tiraram média maior ou igual a 9,0
    def teste_media(self):
        retorno = [('algoritmos',),
                   ('estrutura de dados',)]
        self.assertEqual(alunos_media(self.mock_db_config.get('bd'), 9.0), retorno)
    # Teste para ver se irá retornar vazio, quando não existir ou quando for zero:
    def teste_existe(self):
        retorno = []
        self.assertEqual(alunos_media(self.mock_db_config.get('bd'), 0.0), retorno)

    # 2. Listar todas as turmas (nome) e a média final (media) cursadas por um aluno (por exemplo, 'Carla')
    def teste_carla(self):
        retorno = [('estrutura de dados', 9.6,),
                 ('algoritmos', 5.2),
                 ('sistemas digitais', 7.1,)]
        self.assertEqual(turmas_carla(self.mock_db_config.get('bd'), 'Carla'), retorno)
    # Teste para ver se irá retornar vazio, quando não existir um aluno:
    def teste_existe(self):
        retorno = []
        self.assertEqual(turmas_carla(self.mock_db_config.get('bd'), 'Xuxa'), retorno)

    # 1. Encontrar a maior média já vista em uma turma de código TAD0203
    def teste_maior_media(self):
        retorno = [(9.0,)]
        self.assertEqual(maior_media(self.mock_db_config.get('bd'), 'TAD0203'), retorno)

    # Teste para ver se irá retornar vazio, quando não existir a turma indicada:
    def teste_existe(self):
        retorno = [(None,)]
        self.assertEqual(maior_media(self.mock_db_config.get('bd'), 'TAD0000'), retorno)