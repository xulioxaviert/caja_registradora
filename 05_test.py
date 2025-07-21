# Variable para almacenar los nombres
nombres = []

# Función para agregar nombres a la lista
def agregar_nombre(cadena_texto):
    nuevos_nombres = cadena_texto.split(',')
    for nombre in nuevos_nombres:
        nombres.append(nombre.strip())

# Función para mostrar todos los nombres
def mostrar_nombres():
    print("Lista de nombres:")
    for nombre in nombres:
        print(f"- {nombre}")

# Función para buscar nombres que comienzan con una letra específica
def buscar_por_letra(letra):
    print(f"Nombres que comienzan con '{letra}':")
    for nombre in nombres:
        if nombre.startswith(letra):
            print(f"- {nombre}")

# Función para contar la cantidad de nombres
def contar_nombres():
    return len(nombres)

# Prueba del programa
agregar_nombre("Ana, Alberto, Beatriz, Carlos, Alicia, Xulio, Juan")
mostrar_nombres()
buscar_por_letra("C")
print(f"Cantidad total de nombres: {contar_nombres()}")
