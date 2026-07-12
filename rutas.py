import requests
import urllib.parse

key = "00c4642a-ed76-43e2-9207-0a5008968c8b"
geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url = "https://graphhopper.com/api/1/route?"

def geocoding(location):
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})
    datos = requests.get(url).json()
    lat = datos["hits"][0]["point"]["lat"]
    lng = datos["hits"][0]["point"]["lng"]
    return lat, lng

while True:
    origen = input("Ciudad de Origen (o 's' para salir): ")
    if origen.lower() == "s":
        print("Saliendo del programa.")
        break
    destino = input("Ciudad de Destino: ")
    if destino.lower() == "s":
        print("Saliendo del programa.")
        break
        
    print("\nMedios de transporte disponibles: car, bike, foot")
    vehiculo = input("Elija el medio de transporte: ")
    if vehiculo not in ("car", "bike", "foot"):
        vehiculo = "car"
        print("Opcion no valida, se usara 'car' por defecto.")
        
    lat1, lng1 = geocoding(origen)
    lat2, lng2 = geocoding(destino)
    
    punto_origen = "&point=" + str(lat1) + "," + str(lng1)
    punto_destino = "&point=" + str(lat2) + "," + str(lng2)
    
    url_ruta = route_url + urllib.parse.urlencode({"key": key, "vehicle": vehiculo, "locale": "es"}) + punto_origen + punto_destino
    
    datos_ruta = requests.get(url_ruta).json()
    
    km = datos_ruta["paths"][0]["distance"] / 1000
    millas = km / 1.61
    tiempo_ms = datos_ruta["paths"][0]["time"]
    horas = int(tiempo_ms / 1000 / 60 / 60)
    minutos = int(tiempo_ms / 1000 / 60 % 60)
    segundos = int(tiempo_ms / 1000 % 60)
    
    print("\n=================================================")
    print("Viaje de", origen, "a", destino, "en", vehiculo)
    print("Distancia:", round(km, 1), "km /", round(millas, 1), "millas")
    print("Duracion:", horas, "h", minutos, "min", segundos, "seg")
    print("=================================================")
    print("Narrativa del viaje:")
    for paso in datos_ruta["paths"][0]["instructions"]:
        print("-", paso["text"])
    print("=================================================\n")
