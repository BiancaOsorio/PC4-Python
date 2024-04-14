import sqlite3
import requests
from datetime import date

# Función para obtener los precios del Bitcoin en diferentes monedas
def obtener_precios_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    precios = {
        "USD": float(data["bpi"]["USD"]["rate"].replace(",", "")),
        "GBP": float(data["bpi"]["GBP"]["rate"].replace(",", "")),
        "EUR": float(data["bpi"]["EUR"]["rate"].replace(",", ""))
    }
    return precios

# Función para obtener el tipo de cambio PEN/USD desde la API de SUNAT
def obtener_tipo_cambio_pen_usd():
    # Aquí realizarías la solicitud a la API de SUNAT para obtener el tipo de cambio PEN/USD
    # Supongamos que ya tienes la función implementada y devuelve el tipo de cambio
    return 3.8  # Esto es un valor de ejemplo

# Función para crear la tabla bitcoin si no existe
def crear_tabla():
    conn = sqlite3.connect('bitcoin.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha DATE,
                        precio_usd REAL,
                        precio_gbp REAL,
                        precio_eur REAL,
                        precio_pen REAL
                    )''')
    conn.commit()
    conn.close()

# Función para insertar los precios del bitcoin en la tabla
def insertar_precios(fecha, precios):
    conn = sqlite3.connect('bitcoin.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur) 
                      VALUES (?, ?, ?, ?)''', (fecha, precios["USD"], precios["GBP"], precios["EUR"]))
    conn.commit()
    conn.close()

# Función para calcular y actualizar el precio del bitcoin en PEN
def actualizar_precio_pen(fecha):
    conn = sqlite3.connect('bitcoin.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT precio_usd FROM bitcoin WHERE fecha = ?''', (fecha,))
    precio_usd = cursor.fetchone()[0]
    tipo_cambio_pen_usd = obtener_tipo_cambio_pen_usd()
    precio_pen = precio_usd * tipo_cambio_pen_usd
    cursor.execute('''UPDATE bitcoin SET precio_pen = ? WHERE fecha = ?''', (precio_pen, fecha))
    conn.commit()
    conn.close()

# Función para consultar el precio de comprar 10 bitcoins en PEN y EUR
def consultar_precio_compra():
    conn = sqlite3.connect('bitcoin.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT precio_pen * 10 AS precio_compra_pen, precio_eur * 10 AS precio_compra_eur 
                      FROM bitcoin WHERE fecha = ?''', (date.today(),))
    precios = cursor.fetchone()
    conn.close()
    return precios

# Ejemplo de uso de las funciones
crear_tabla()
precios = obtener_precios_bitcoin()
insertar_precios(date.today(), precios)
actualizar_precio_pen(date.today())
precio_compra = consultar_precio_compra()
print("Precio de comprar 10 bitcoins en PEN:", precio_compra[0])
print("Precio de comprar 10 bitcoins en EUR:", precio_compra[1])