from unittest import TestCase

import sys
sys.path.insert(0, '..')
from conexaoDB import *

BD = "TestBD.db"

class MockBD(TestCase):
    @classmethod
    def setUpClass(cls):
        con = conectar(BD)
        cursor = con.cursor()

        # Professor: id(PK), nome
        # Turma: id(PK), nome, codigo
        # Aluno: id(PK), nome
        # Media_aluno_turma: id(PK), id_turma(FK), id_aluno (FK), nota1, nota2, nota3, media

        #query_create_professor = """CREATE TABLE Professor (
        #                              id int NOT NULL PRIMARY KEY ,
        #                              nome text NOT NULL
        #                              )"""
        query_create_turma = """CREATE TABLE Turma (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL, 
                                  codigo string NOT NULL
                                )"""
        query_create_aluno = """CREATE TABLE Aluno (
                                  id int NOT NULL PRIMARY KEY ,
                                  nome text NOT NULL
                                )"""
        query_create_media_aluno_turma = """CREATE TABLE Media_aluno_turma (
                                  id int NOT NULL PRIMARY KEY ,
                                  id_turma int NOT NULL,
                                  id_aluno int NOT NULL,
                                  nota1 float NOT NULL,
                                  nota2 float NOT NULL,
                                  nota3 float NOT NULL,
                                  media float NOT NULL,
                                  FOREIGN KEY (id_turma) REFERENCES Turma(id),
                                  FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
                                )"""
        try:
        #    cursor.execute(query_create_professor)
            cursor.execute(query_create_turma)
            cursor.execute(query_create_aluno)
            cursor.execute(query_create_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na criação das tabelas:", error)
        else:
            print("Criação das tabelas: OK")

        #query_insert_professor = """INSERT INTO Professor (id, nome) VALUES
        #                            (1, 'Leonardo'),
        #                            (2, 'Alessandra'),
        #                            (3, 'Taniro'),
        #                            (4, 'Tasia')"""
        query_insert_turma = """INSERT INTO Turma (id, nome, codigo) VALUES
                                    (1, 'sistemas digitais','TAD0908'),
                                    (2, 'algoritmos', 'TAD0203'),
                                    (3, 'estrutura de dados', 'TAD9874'),
                                    (4, 'estatistica', 'TAD3443')"""
        query_insert_aluno = """INSERT INTO Aluno (id, nome) VALUES
                                    (1, 'Emilly'),
                                    (2, 'Carla'),
                                    (3, 'Carol'),
                                    (4, 'Angela'),
                                    (5, 'Danilo'),
                                    (6, 'Rafael')"""
        query_insert_media_aluno_turma = """INSERT INTO Media_aluno_turma (id, id_turma, id_aluno, nota1, nota2, nota3, media) VALUES
                                    (1, 2, 1, 9.8, 7.6, 9.6, 9.0),
                                    (2, 3, 2, 10.0, 9.0, 9.8, 9.6),
                                    (3, 2, 3, 8.8, 8.5, 9.4, 8.9),
                                    (4, 3, 4, 9.8, 8.5, 9.3, 9.2),
                                    (5, 2, 5, 8.7, 9.8, 5.5, 8.0),
                                    (6, 4, 6, 5.5, 4.0, 5.5, 5.0),
                                    (7, 2, 2, 5.3, 7.0, 3.3, 5.2),
                                    (8, 1, 4, 5.3, 6.2, 6.5, 6.0),
                                    (9, 1, 2, 8.5, 6.4, 6.4, 7.1),
                                    (10, 2, 6, 7.2, 9.5, 8.5, 8.4)"""
        try:
        #    cursor.execute(query_insert_professor)
            cursor.execute(query_insert_turma)
            cursor.execute(query_insert_aluno)
            cursor.execute(query_insert_media_aluno_turma)
            con.commit()
        except sqlite3.Error as error:
            print("Erro na inserção de dados:", error)
        else:
            print("Inserção dos dados: OK")

        cursor.close()

        desconectar(con)

        testconfig ={
            'bd': BD
        }
        cls.mock_db_config = testconfig

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        con = conectar(BD)
        cursor = con.cursor()

        try:
        #    cursor.execute("DROP TABLE Professor")
            cursor.execute("DROP TABLE Turma")
            cursor.execute("DROP TABLE Aluno")
            cursor.execute("DROP TABLE Media_aluno_turma")
            con.commit()
            cursor.close()
            print("Removeu os dados das tabelas.")
        except sqlite3.Error as error:
            print("Banco de dados não existe. Erro na remoção do BD.", error)
        finally:
            desconectar(con)