def obtener_lista_estudiantes_ordenada(aulas):
    lista_desordenada = []
    lista_de_nombres = []

    for aulas, estudiantes in aulas.items():
        for estudiante in estudiantes:
            promedio = sum(estudiante["notas"])/len(estudiante["notas"])
            estudiantes_con_promedio = estudiante.copy()
            estudiantes_con_promedio["promedio_notas"] = promedio
            lista_desordenada.append(estudiantes_con_promedio)

    lista_ordenada = sorted(lista_desordenada, key=lambda x: x['promedio_notas'], reverse=True)
    for estudiante in lista_ordenada:
        lista_de_nombres.append(estudiante["nombre"])
    return lista_de_nombres

def obtener_lista_estudiantes_ordenada2(aulas):
    lista_desordenada = []
    lista_de_nombres = []
    for aulas, estudiantes in aulas.items():
        for estudiante in estudiantes:
            promedio = sum(estudiante['notas'])/len(estudiante['notas'])
            estudiantes_con_promedio = estudiante.copy()
            estudiantes_con_promedio['promedio'] = promedio
            lista_desordenada.append(estudiantes_con_promedio)

    lista_ordenada = sorted(lista_desordenada, key=lambda x: x['promedio'], reverse=True)
    # sorted(iterable, key=None, reverse=True)
    for estudiantes in lista_ordenada:
        lista_de_nombres.append(estudiante['nombre'])
    return lista_de_nombres


def mejor_del_sexo(sexo, aulas):
    estudiantes_por_promedio = obtener_lista_estudiantes_ordenada(aulas)
    for estudiante in estudiantes_por_promedio:
        for estudiantes in aulas.values():
            for student in estudiantes:
                if student['sexo'] == sexo and student['nombre'] == estudiante:
                    return estudiante

# print(mejor_del_sexo('masculino', aulas = {
#     'aula 1': [
#     {'nombre': 'Ramiro', 'sexo': 'masculino', 'notas': [2, 3, 4]},
#     {'nombre': 'Juan', 'sexo': 'masculino', 'notas': [3, 5, 7]}
#     ]
#     }))


print(obtener_lista_estudiantes_ordenada2(aulas = {
    'aula 1': [
    {'nombre': 'Ramiro', 'sexo': 'masculino', 'notas': [2, 3, 4]},
    {'nombre': 'Juan', 'sexo': 'masculino', 'notas': [3, 5, 7]}
    ]
    }))
