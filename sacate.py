# Diccionario con estudiantes
estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    materias = input("Ingrese las materias aprobadas (separadas por coma): ").split(",")
    estudiantes[nombre] = {"edad": edad, "materias": [materia.strip() for materia in materias]}
    print(f"Estudiante {nombre} agregado con éxito.\n")

# Función para mostrar la lista de estudiantes
def mostrar_estudiantes():
    if estudiantes:
        print("\nLista de estudiantes:")
        for nombre, datos in estudiantes.items():
            print(f"Nombre: {nombre}")
            print(f"Edad: {datos['edad']}")
            print(f"Materias aprobadas: {', '.join(datos['materias'])}")
            print("-" * 30)
    else:
        print("No hay estudiantes registrados.\n")

# Función para eliminar un estudiante
def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado con éxito.\n")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.\n")

# Función para buscar un estudiante por nombre
def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"\nEstudiante encontrado: {nombre}")
        print(f"Edad: {datos['edad']}")
        print(f"Materias aprobadas: {', '.join(datos['materias'])}\n")
    else:
        print(f"No se encontró un estudiante con el nombre {nombre}.\n")

# Función para verificar si una palabra clave está en el nombre de algún estudiante
def buscar_palabra_clave():
    clave = input("Ingrese una palabra clave para buscar en los nombres: ").lower()
    encontrado = False
    for nombre in estudiantes.keys():
        if clave in nombre.lower():
            print(f"Estudiante encontrado: {nombre}")
            encontrado = True
    if not encontrado:
        print(f"No se encontró ninguna coincidencia con la palabra clave '{clave}'.\n")

# Menú principal
def menu():
    opcion = ""
    while opcion != "6":
        print("Menú de opciones:")
        print("1. Agregar un nuevo estudiante")
        print("2. Mostrar la lista de estudiantes")
        print("3. Eliminar un estudiante")
        print("4. Buscar un estudiante por nombre")
        print("5. Buscar palabra clave en los nombres de estudiantes")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                agregar_estudiante()
            case "2":
                mostrar_estudiantes()
            case "3":
                eliminar_estudiante()
            case "4":
                buscar_estudiante()
            case "5":
                buscar_palabra_clave()
            case "6":
                print("¡Gracias por usar el programa!")
            case _:
                print("Opción no válida. Intente nuevamente.\n")

# Llamamos al menú para iniciar el programa
menu()
