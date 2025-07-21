# Declaración de variables para almacenar los nombres y notas
estudiantes = []
notas_estudiantes = {}

# Definimos las funciones que vamos a necesitar para el proyecto
def calcular_promedio(notas):
    return sum(notas)/len(notas)

def determinar_estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar:)")
    if nombre.lower() == 'salir':
        break
    estudiantes.append(nombre)
    notas = []
    while True:
        nota = input("Ingrese la nota del estudiante (o 'salir' para terminar:)")
        if nota.lower()=='salir':
            break
        nota_decimal = float(nota)
        notas.append(nota_decimal)
        notas_estudiantes[nombre] = notas    
print(notas_estudiantes)

#Calcular promedios e imprimir los resultados
print("Resultados:")
for estudiante in estudiantes:
    notas = notas_estudiantes[estudiante]
    promedio = calcular_promedio(notas)
    estado = determinar_estado(promedio)
    print(f"Las notas: {notas}")
    print(f"El promedio: {promedio}")
    print(f"Estado: {estado}")