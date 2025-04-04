# Diccionario de estudiantes
estudiantes = {
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
}

def agregar_estudiante():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    materias = input("Materias aprobadas (separadas por coma): ").split(",")
    estudiantes[nombre] = {"edad": edad, "materias": [m.strip() for m in materias]}
    print(f"{nombre} agregado.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return
    for nombre, datos in estudiantes.items():
        print(f"{nombre} | Edad: {datos['edad']} | Materias: {', '.join(datos['materias'])}")

def eliminar_estudiante():
    nombre = input("Nombre del estudiante a eliminar: ")
    if estudiantes.pop(nombre, None):
        print(f"{nombre} eliminado.\n")
    else:
        print(f"{nombre} no encontrado.\n")

def buscar_estudiante():
    nombre = input("Nombre a buscar: ")
    if nombre in estudiantes:
        datos = estudiantes[nombre]
        print(f"{nombre} | Edad: {datos['edad']} | Materias: {', '.join(datos['materias'])}\n")
    else:
        print(f"{nombre} no encontrado.\n")

def buscar_palabra_clave():
    clave = input("Palabra clave: ").lower()
    coincidencias = [n for n in estudiantes if clave in n.lower()]
    print("\n".join(coincidencias) if coincidencias else "No hay coincidencias.\n")

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
menu ()
