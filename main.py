import os
from pathlib import Path
from os import system

my_ruta = Path(Path.home(), "Documents", "Adm Recetas", "Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():
    system("cls")
    print("="*46)
    print("*" * 3 + " Bienvenido al administrador de recetas " + "*" * 3)
    print("="*46)
    print("\n")
    print(f"Las recetas se encuentran en: {my_ruta}")
    print(f"Actualmente tienes {contar_recetas(my_ruta)} recetas guardadas")
    
    #se hace un while para validar la entrada del usuario, se coloca lo que no queremos que suceda.
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("\n")
        print("Elige una opción del menú:")
        print("""
        1. Ver recetas
        2. Crear receta
        3. Crear categoría
        4. Eliminar receta
        5. Eliminar categorías
        6. Salir
        """)
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print("Categorías disponibles:")
    ruta_categorias = Path(ruta)
    Lista_Categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        Lista_Categorias.append(carpeta)
        contador += 1
    return Lista_Categorias

def elegir_categoria(lista):
    eleccion_categoria = "x"
    while not eleccion_categoria.isnumeric() or int(eleccion_categoria) not in range(1, len(lista)+1):
        eleccion_categoria = input("\nElige una categoría:")
    return lista[int(eleccion_categoria)-1]

def mostrar_recetas(ruta):
    print("Recetas disponibles:")
    ruta_recetas = Path(ruta)
    Lista_Recetas = []
    contador = 1
    for receta in ruta_recetas.glob("**/*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        Lista_Recetas.append(receta)
        contador += 1
    return Lista_Recetas

def elegir_receta(lista):
    eleccion_receta = "x"
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range (1, len(lista)+1):
        eleccion_receta = input("\nElige una receta:")
    return lista[int(eleccion_receta)-1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la receta:")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta:")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Esa receta ya existe, elige otro nombre")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de la categoria:")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Esa categoría ya existe, elige otro nombre")

def eliminar_receta(receta):
    Path.unlink(receta)
    print(f"La receta {receta.name} ha sido eliminada.")

def eliminar_categoria(categoria):
    Path.rmdir(categoria)
    print(f"La categoría {categoria.name} ha sido eliminada.")

def volver_inicio():
    eleccion = "x"
    while eleccion.lower() != "v":
        eleccion = input("Pulsa 'v' para volver al menú.")



finaliza_programa = False
while not finaliza_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(my_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(my_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(my_ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(my_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(my_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        finaliza_programa = True

