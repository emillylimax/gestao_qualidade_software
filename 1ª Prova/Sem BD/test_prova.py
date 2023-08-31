from prova import *
import unittest

#TESTE SEM BANCO:
#Questão 1:
class MaiorNota(unittest.TestCase):
    def test_encontrar_alunos_maior_nota(self):
        notas = [('Carla', 9.7), ('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 9.7), ('Flávio', 5.7), ('Silvia', 4.4)]
        retorno_esperado = ['Carla', 'Alice']
        self.assertEqual(encontrar_alunos_maior_nota (notas), retorno_esperado)
#Teste para retornar apenas uma pessoa:
    def test_erro(self):
        notas = [('Carla', 9.7), ('Danilo', 6.7), ('Daniel', 3.4), ('Alice', 8.7), ('Flávio', 5.7), ('Silvia', 4.4)]
        retorno_esperado = ['Carla']
        self.assertEqual(encontrar_alunos_maior_nota (notas), retorno_esperado)

#Questão 4:
class TestPercentual(unittest.TestCase):
    def test_percentual_acima_de_sete(self):
        notas_turmas = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4), ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7), ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]
        retorno_esperado ={1: 50, 2: 66.67, 3: 0}
        self.assertEqual(percentual (notas_turmas), retorno_esperado)

#Questão 3:
class MediaNotasPorProfessor(unittest.TestCase):
    def test_notas_professor(self):
        notas_turmas = [('TAD0055', 1, 9.7), ('TAD0010', 2, 6.7), ('TAD0105', 3, 3.4), ('TAD0105', 1, 4.4), ('TAD0105', 2, 7.1), ('TAD0027', 2, 9.7), ('TAD0202', 3, 5.7), ('TAD0001', 3, 4.4)]
        resultado_esperado = {1: 7.05, 2: 7.83, 3: 4.5}
        self.assertEqual(notas_professor(notas_turmas), resultado_esperado)