#Questão 1:
def encontrar_alunos_maior_nota(notas):
    maior_nota = max(nota for aluno, nota in notas)
    alunos_maior_nota = [aluno for aluno, nota in notas if nota == maior_nota]
    return alunos_maior_nota

#Questão 4:
def percentual(notas_turmas):
    perc_por_professor = {}
    for _, id_professor, media in notas_turmas:
        perc_por_professor.setdefault(id_professor, []).append(media > 7.0)

    for id_professor, percentuais in perc_por_professor.items():
        total_turmas = len(percentuais)
        percentual = sum(percentuais) / total_turmas * 100
        perc_por_professor[id_professor] = round(percentual, 2)

    return perc_por_professor

#Questão 3:
def notas_professor(notas_turmas):
    notas_por_professor = {}
    cont_por_professor = {}

    for turma, id_professor, media in notas_turmas:
        if id_professor not in notas_por_professor:
            notas_por_professor[id_professor] = 0
            cont_por_professor[id_professor] = 0
        notas_por_professor[id_professor] += media
        cont_por_professor[id_professor] += 1

    media_notas_por_professor = {}
    for id_professor in notas_por_professor:
        media = notas_por_professor[id_professor] / cont_por_professor[id_professor]
        media_notas_por_professor[id_professor] = round(media, 2)

    return media_notas_por_professor