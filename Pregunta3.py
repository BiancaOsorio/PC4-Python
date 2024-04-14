import requests
import zipfile
from io import BytesIO

# Función para descargar la imagen desde el URL
def descargar_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Error al descargar la imagen:", response.status_code)
        return None

# Función para comprimir la imagen en un archivo ZIP
def comprimir_zip(nombre_archivo, contenido):
    with zipfile.ZipFile(nombre_archivo, 'w') as zipf:
        zipf.writestr("imagen.jpg", contenido)

# Función para descomprimir un archivo ZIP
def descomprimir_zip(nombre_archivo):
    with zipfile.ZipFile(nombre_archivo, 'r') as zipf:
        zipf.extractall("imagenes_extraidas")

# URL de la imagen a descargar
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Descargar la imagen desde el URL
contenido_imagen = descargar_imagen(url_imagen)

if contenido_imagen:
    # Comprimir la imagen en un archivo ZIP
    nombre_archivo_zip = "imagen_comprimida.zip"
    comprimir_zip(nombre_archivo_zip, contenido_imagen)
    print("Imagen comprimida como:", nombre_archivo_zip)

    # Descomprimir el archivo ZIP
    descomprimir_zip(nombre_archivo_zip)
    print("Archivo ZIP descomprimido.")