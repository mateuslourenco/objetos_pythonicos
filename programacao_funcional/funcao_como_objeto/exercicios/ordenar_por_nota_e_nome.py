"""
Construa uma função de ordenação que ordene os alunos por nota. Se houver empate em nota, o nome deverá definir a ordem

>>> alunos = [('Renzo', 0), ('Luciano', 10),('Renzo Santos', 10), ('Renzo Nuccitelli', 10)]
>>> alunos.sort(key=ordenar_por_nota_e_nome)
>>> alunos
[('Renzo', 0), ('Luciano', 10), ('Renzo Nuccitelli', 10), ('Renzo Santos', 10)]
"""


def ordenar_por_nota_e_nome(aluno):
    nome, nota = aluno
    return nota, nome
