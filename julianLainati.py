#Gestión de Inventario y Ventas de una Librería
#caso (problema): Una libreria necesita desarrollar una aplicación que permita registrar libros en el inventario y realizar ventas
tipos = ["Ficción", "No Ficción", "Ciencia"]
ventas = []
libros = []

def elegir_tipos():
    print("1. Ficción\n 2. No Ficción\n 3. Ciencia")
    opcion = int(input("Elige un tipo: "))
    if opcion in range(1, 4):
        return tipos[opcion - 1]
    else:
        print("Opción no válida")
        return elegir_tipos()

def registrar_libro():
    nombre = input("Introduce el título del libro: ").upper()
    escritor = input("Introduce el autor del libro: ").upper()
    tipo = elegir_tipos()
    try:
        costo = int(input("Introduce el precio del libro: "))
        cantidad = int(input("Introduce la cantidad en stock: "))
    except ValueError:
        print("Entrada inválida")
        return
    nuevo_libro = [nombre, escritor, tipo, costo, cantidad]
    libros.append(nuevo_libro)

def listar_libros():
    print("Título\t\tAutor\t\tTipo\t\tPrecio\t\tStock")

def registrar_venta():
    nombre_libro = input("Introduce el título del libro a vender: ").upper()
    for libro in libros:
        if libro[0] == nombre_libro:
            try:
                cantidad = int(input("Introduce la cantidad a vender: "))
            except ValueError:
                print("Entrada inválida")
                return
            if cantidad > libro[4]:
                print("Stock insuficiente")
                return
            total = cantidad * libro[3]
            libro[4] -= cantidad
            tipo = libro[2]
            print(f"Detalle:\nLibro: {nombre_libro}\nPrecio unitario: {libro[3]}\nCantidad: {cantidad}\nTotal: {total}")
            nueva_venta = [nombre_libro, tipo, cantidad]
            ventas.append(nueva_venta)
            return
    print("Libro no encontrado")

def Imprimir_reporte():
    print("1. Reporte completo\n2. Reporte por tipo")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        print("Título\t\tTipo\t\tCantidad vendida")
        for venta in ventas:
            print(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}")
    elif opcion == 2:
        tipo = elegir_tipos()
        print("Título\t\tTipo\t\tCantidad vendida")
        for venta in ventas:
            if venta[1] == tipo:
                print(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}")
    else:
        print("Opción no válida")

def Generar_Texto():
    print("1. Reporte completo\n2. Reporte por tipo")
    opcion = int(input("Elige una opción para el reporte: "))
    with open("ventas.txt", "w") as archivo:
        if opcion == 1:
            archivo.write("Título\t\tTipo\t\tCantidad vendida\n")
            for venta in ventas:
                archivo.write(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}\n")
        elif opcion == 2:
            tipo = elegir_tipos()
            archivo.write("Título\t\tTipo\t\tCantidad vendida\n")
            for venta in ventas:
                if venta[1] == tipo:
                    archivo.write(f"{venta[0]}\t\t{venta[1]}\t\t{venta[2]}\n")
        else:
                        print("Opción no válida")
    print("Reporte generado exitosamente")

def menu():
    while True:
        print("(1) Registrar libro\n(2) Listar todos libros\n(3) Registrar venta\n(4) Imprimir reporte de ventas\n(5) Generar texto\n(6) Salir del programa")
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Entrada no válida")
            continue
        if opcion == 1:
            registrar_libro()
        elif opcion == 2:
            listar_libros()
        elif opcion == 3:
            registrar_venta()
        elif opcion == 4:
            Imprimir_reporte()
        elif opcion == 5:
            Generar_Texto()
        elif opcion == 6:
            break
        else:
            print("Opción no válida")

menu()

    