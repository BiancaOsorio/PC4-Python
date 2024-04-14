import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanza una excepción en caso de error en la solicitud
        data = response.json()
        precio = float(data["bpi"]["USD"]["rate"].replace(",", ""))  # Extrae el precio en USD y convierte a float
        return precio
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def calcular_costo_en_usd(cantidad_bitcoins, precio_bitcoin):
    costo_usd = cantidad_bitcoins * precio_bitcoin
    return costo_usd

def main():
    cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_usd = calcular_costo_en_usd(cantidad_bitcoins, precio_bitcoin)
        print(f"El costo actual de {cantidad_bitcoins:g} Bitcoins es: ${costo_usd:.4f}")
if __name__ == "__main__":
    main()