def guardar_tabla_multiplicar(numero):
    with open(f"tabla-{numero}.txt", 'w') as archivo:
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", 'r') as archivo:
            print(f"Tabla de multiplicar del {numero}:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", 'r') as archivo:
            lineas = archivo.readlines()
            if linea <= len(lineas):
                print(f"Línea {linea}: {lineas[linea - 1].strip()}")
            else:
                print(f"La tabla de multiplicar del {numero} tiene menos de {linea} líneas.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número ingresado no está dentro del rango válido.")
        elif opcion == '2':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("El número ingresado no está dentro del rango válido.")
        elif opcion == '3':
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                linea = int(input("Ingrese el número de línea que desea ver: "))
                mostrar_linea_tabla(numero, linea)
            else:
                print("El número ingresado no está dentro del rango válido.")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    menu()