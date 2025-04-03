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
    while True:
        print("\n1. Agregar\n2. Mostrar\n3. Eliminar\n4. Buscar\n5. Buscar palabra clave\n6. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            eliminar_estudiante()
        elif opcion == "4":
            buscar_estudiante()
        elif opcion == "5":
            buscar_palabra_clave()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.\n")

menu()

