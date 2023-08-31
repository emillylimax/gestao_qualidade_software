from conexaoDB import *

# Listar o nome das turmas que tiveram alunos que tiraram média maior ou igual a 9,0
def alunos_media(bd, media):
    query = "SELECT DISTINCT t.nome " \
           "FROM Turma t, Media_aluno_turma m " \
           "WHERE m.media >= ? AND m.id_turma = t.id"
    return ler_bd(bd, query, (media,))

# Listar todas as turmas (nome) e a média final (media) cursadas por um aluno (por exemplo, 'Carla')
def turmas_carla(bd, nome):
    query = "SELECT t.nome, m.media " \
            "FROM Turma t, Media_aluno_turma m, Aluno a " \
            "WHERE a.nome LIKE ? AND m.id_turma = t.id AND m.id_aluno = a.id"
    return ler_bd(bd, query, ('%'+nome+'%',))

# Encontrar a maior média já vista em uma turma de código TAD0203
def maior_media(bd, turma):
    query = "SELECT MAX(m.media) " \
            "FROM Media_aluno_turma m, Turma t " \
            "WHERE t.codigo LIKE ? AND m.id_turma=t.id"
    return ler_bd(bd, query, ('%'+turma+'%',))