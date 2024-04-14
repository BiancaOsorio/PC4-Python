import requests
import sqlite3

# Función para obtener los datos del API de SUNAT
def obtener_datos_sunat(year):
    url = f"https://api.apis.net.pe/v1/tipo-cambio/{year}/dolares"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos del API de SUNAT:", response.status_code)
        return None

# Función para crear la base de datos y la tabla si no existen
def crear_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        compra REAL,
                        venta REAL
                    )''')
    conn.commit()
    conn.close()

# Función para insertar los datos en la tabla
def insertar_datos(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    for dato in datos:
        fecha = dato['fecha']
        compra = dato['compra']
        venta = dato['venta']
        cursor.execute("INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    conn.commit()
    conn.close()

# Función para mostrar el contenido de la tabla
def mostrar_contenido():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    conn.close()

# Año para el cual obtener el tipo de cambio
year = 2023

# Obtener los datos del API de SUNAT
datos = obtener_datos_sunat(year)
if datos:
    # Crear la tabla si no existe
    crear_tabla()
    
    # Insertar los datos en la tabla
    insertar_datos(datos)
    
    # Mostrar el contenido de la tabla
    print("Contenido de la tabla sunat_info:")
    mostrar_contenido()
else:
    print("No se pudieron obtener los datos del API de SUNAT.")