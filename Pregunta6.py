def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            lineas_limpias = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith("#")]
            return len(lineas_limpias)
    except FileNotFoundError:
        print("¡El archivo no fue encontrado!")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")

    if not ruta_archivo.endswith('.py'):
        print("El archivo no tiene extensión .py")
        return

    cantidad_lineas = contar_lineas_codigo(ruta_archivo)

    if cantidad_lineas is not None:
        print(f"El archivo '{ruta_archivo}' tiene {cantidad_lineas} líneas de código.")

if __name__ == "__main__":
    main()