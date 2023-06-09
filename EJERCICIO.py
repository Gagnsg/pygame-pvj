class Menu:
    def __init__(self):
        self.opcion = ''

    def mostrar_menu(self):
        print("----- MENÚ -----")
        print("1. Seleccionar cliente")
        print("2. Insertar cliente")
        print("3. Editar cliente")
        print("4. Borrar cliente")
        print("5. Salir")

    def seleccionar_opcion(self, opcion):
        if opcion == '1':
            print("Has seleccionado la opción 1: Seleccionar cliente")
        elif opcion == '2':
            print("Has seleccionado la opción 2: Insertar cliente")

        elif opcion == '3':
            print("Has seleccionado la opción 3: Editar cliente")
        elif opcion == '4':
            print("Has seleccionado la opción 4: Borrar cliente")
        elif opcion == '5':
            print("Has seleccionado la opción 5: Salir")
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

menu = Menu()

while menu.opcion != '5':
    menu.mostrar_menu()
    menu.opcion = input("Selecciona una opción: ")
    menu.seleccionar_opcion(menu.opcion)
