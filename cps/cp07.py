# Diccionarios y conjuntos
# CACHARREO CON NOTES07

def cacharreo_c07():
    diccionario = {}
    alumno = {
    'nombre': 'Ana', #key: value
    'id_matricula': 12345, 
    'curso_actual': 'Programación I', 
    "activa": True
    }

    nombre = alumno.get('nombre', 'no especificado')
    alumno['nombre'] = 'Cynthia'
    alumno['otra clave'] = 'otro valor' #añade un nuevo par
    alumno.update({'campus': 'UH', 'promedio': 10})
    config_adicional = {'beca': True, 'activa': False, 'asistencia': "100%"}
    alumno.update(config_adicional)

    print(alumno['activa'])
    print(alumno)
    print(nombre)

    deletion_test = alumno.pop('clave inexistente', 'jaja')
    '''
    pop es mas seguro que del porque permite asignar valor 
    por defecto y devuelve None por defecto. del devuelve TypeError
    '''
    print(deletion_test)
    print('nombre' in alumno) #comprueba existencia de claves, no valores
    for clave in alumno:
        print(clave)
    for valor in alumno.values():
        print(valor)
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")

#EJERCICIOS DE LA WEB Y DEEPSEEK
def estudiantes():
    estudiantes = {'edad': 10, 'carrera': 'CC'}
    print(estudiantes)
    for clave in estudiantes:
        print(clave)
    for valor in estudiantes.values():
        print(valor)
    estudiantes['carrera'] = 'Matematicas'
    estudiantes.update({'universidad': 'UH'})
    print(estudiantes   )

def inventario():
    inventario = {'manzanas': 2, 'guayabas': 4, 'peras': 5}
    inventario['guayabas'] += 3
    inventario.pop('manzanas')
    inventario.update({'peras': 7})
    uvas = inventario.get('uvas', 'no hay uvas en el inventario')
    print(inventario)
    print(uvas)


def frecuencia_letras():
    palabra = input("palabra?\n")
    frecuencia = {}
    # variable = 3
    # dict = {'eee': variable}
    # print(dict)
    for letra in palabra:
        if letra != ' ':
            if letra not in frecuencia:
                frecuencia[letra] = 1
            else:
                frecuencia[letra] += 1
    print(frecuencia)


def datos():
    nombre = input("nombre?").lower()
    edad = int(input("edad?"))
    telefono = int(input("telefon?"))
    datos = {'nombre': nombre, 'edad': edad, 'telefono': telefono}
    print(f"{nombre}, {edad}, {telefono}")

#EJERCICIOS CP07
def contando():
    enteros = [1, 2, 3, 8, 1, 1, 8, 8, 8]
    counter = {}
    for number in enteros:
        if number not in counter:
            counter[number] = 1
        else:
            counter[number] += 1
    print('Numeros repetidos mas de 2 veces:')
    for clave, valor in counter.items():
        if valor > 2:
            print(f'{clave} se repite {valor} veces')
# contando()
    
def mapas_traducciones(dictionary, lista):
    oracion = ""

    for entero in lista:
        if entero in dictionary:
            oracion += dictionary[entero] + " "
    return oracion

#Hacer un método, al que le entra una lista de números y 
#tiene que devolver la cantidad de números diferentes
# Ejemplo:
# - input: 22222
# - output: 1
def pe_jueves23(numeros):
    return len(set(numeros))

#Dada una matriz en forma de lista de listas donde en cada posición se guarda un valor entero o None, 
#devuelve una matriz dispersa con los enteros almacenados en la original
def dispersion(matriz):
    dispersa = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != None:
                dispersa[(i, j)] = matriz[i][j]
    return dispersa

# print(dispersion([[1, None], [2], [None]]))

# TODO def informe_costos():

'''
testimonios = [
 {'age': [23, 40, 30]},
 {'height': [1.7, 1.6]}
]
'''

def testimonials_convertion(requested_data, testimonials):
    output = []
    for info in requested_data:
        values = set()
        for testimonial in testimonials:
            if info in testimonial:
                values.add(testimonial[info])
        output.append({info: values})
    return output

print(testimonials_convertion(['age', 'height', 'location'], [{'age': 20, 'height': 1.7, 'location': 'park'}, {'height': 2}]))

def averiguaciones(requested_data, testimonials):
    organized_input = testimonials_convertion(requested_data, testimonials)
    contradictions = []
    info_necesaria = True
    for diccionario in organized_input:
        for value in diccionario.values():
            if len(value) == 0:  # error: habia puesto '== []' pero len() devuelve int
                info_necesaria = False
            if len(value) > 1:
                contradictions.append(value)
    return info_necesaria, contradictions


print(averiguaciones(['age', 'height', 'location'], [{'age': 20, 'height': 1.7, 'location': 'park'}, {'height': 2}]))