import os
from pathlib import Path
from os import system

my_ruta = Path(Path.home(), "Documents", "Adm Recetas")

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
    return(eleccion_menu)

inicio() #invoca función



#Mostrar menu de inicio

menu = 0

if menu == 1:
    #mostrar categorías
    #elegir categoría
    #mostrar recetas
    #elegir recetas
    #leer receta
    #volver al menú
    pass
elif menu == 2:
    #mostrar categorías
    #elegir categorías
    #crear receta
    #volver al menú
    pass
elif menu == 3:
    #crear categorías
    pass
elif menu == 4:
    #mostrar categorías
    #elegir categoría
    #mostrar recetas
    #elegir recetas
    #eliminar receta
    #volver al menú
    pass
elif menu == 5:
    #mostrar categorías
    #elegir categoría
    #eliminar categoría
    #volver al menú
    pass
elif menu == 6:
    #salir
    pass

