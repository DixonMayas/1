import sqlite3

def crear_base():
    with sqlite3.connect("sass.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS peliculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT,
                anio INTEGER,
                director TEXT
            )
        ''')
        conn.commit()

def agregar_pelicula():
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    anio = int(input("Anio: "))
    director = input("Director: ")

    with sqlite3.connect("sass.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO peliculas (titulo, genero, anio, director) VALUES (?, ?, ?, ?)",
                       (titulo, genero, anio, director))
        conn.commit()
        print("Pelicula agregada.")

def modificar_pelicula():
    id_pelicula = input("ID de la pelicula a modificar: ")
    nuevo_titulo = input("Nuevo titulo: ")
    nuevo_genero = input("Nuevo genero: ")
    nuevo_anio = int(input("Nuevo anio: "))
    nuevo_director = input("Nuevo director: ")

    with sqlite3.connect("sass.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE peliculas
            SET titulo = ?, genero = ?, anio = ?, director = ?
            WHERE id = ?
        ''', (nuevo_titulo, nuevo_genero, nuevo_anio, nuevo_director, id_pelicula))
        conn.commit()
        print("Pelicula modificada.")

def mostrar_peliculas():
    with sqlite3.connect("sass.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM peliculas")
        peliculas = cursor.fetchall()
        if peliculas:
            for peli in peliculas:
                print(peli)
        else:
            print("No hay peliculas registradas.")

def eliminar_pelicula():
    id_pelicula = input("ID de la pelicula a eliminar: ")
    with sqlite3.connect("sass.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM peliculas WHERE id = ?", (id_pelicula,))
        conn.commit()
        print("Pelicula eliminada.")

def buscar_pelicula():
    titulo = input("Buscar por titulo: ")
    with sqlite3.connect("sass.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM peliculas WHERE titulo LIKE ?", ('%' + titulo + '%',))
        resultados = cursor.fetchall()
        if resultados:
            for peli in resultados:
                print(peli)
        else:
            print("No se encontraron coincidencias.")

def menu():
    crear_base()
    while True:
        print("""
--- MENU ---
1. Agregar pelicula
2. Modificar pelicula
3. Mostrar peliculas
4. Eliminar pelicula
5. Buscar pelicula
6. Salir
""")
        opcion = input("Elegi una opcion: ")

        match opcion:
            case "1":
                agregar_pelicula()
            case "2":
                modificar_pelicula()
            case "3":
                mostrar_peliculas()
            case "4":
                eliminar_pelicula()
            case "5":
                buscar_pelicula()
            case "6":
                print("Hasta luego.")
                break
            case _:
                print("Opcion no valida.")

menu()
