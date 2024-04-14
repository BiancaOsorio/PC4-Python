# Supongamos que tienes una lista de precios de Bitcoin en diferentes monedas
# Cada elemento de la lista es una tupla con la fecha y los precios en USD, GBP, EUR, y PEN
bitcoin_prices = [
    ("2024-04-13", 50000.00, 35000.00, 42000.00, 240000.00),
    # Puedes agregar más datos aquí
]

# Función para escribir los datos en un archivo de texto
def escribir_txt(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        # Escribir datos línea por línea en el archivo de texto
        for dato in datos:
            archivo.write(f"Fecha: {dato[0]}\n")
            archivo.write(f"Precio USD: {dato[1]}\n")
            archivo.write(f"Precio GBP: {dato[2]}\n")
            archivo.write(f"Precio EUR: {dato[3]}\n")
            archivo.write(f"Precio PEN: {dato[4]}\n")
            archivo.write("\n")  # Agregar una línea en blanco entre cada conjunto de datos

# Escribir los datos en un archivo de texto
nombre_archivo = "bitcoin_prices.txt"
escribir_txt(bitcoin_prices, nombre_archivo)
print("Datos de precios de Bitcoin almacenados en:", nombre_archivo)