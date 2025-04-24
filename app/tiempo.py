import random

class Tiempo:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.temperatura_maxima = random.randint(20, 40)  # Temperatura máxima entre 20 y 40 grados
        self.temperatura_minima = random.randint(0, 19)  # Temperatura mínima entre 0 y 19 grados
        self.lluvia = random.choice([True, False])       # True si llueve, False si no
        self.soleado = random.choice([True, False])      # True si está soleado, False si no

    def obtener_datos(self):
        return {
            "ciudad": self.ciudad,
            "temperatura_maxima": self.temperatura_maxima,
            "temperatura_minima": self.temperatura_minima,
            "lluvia": self.lluvia,
            "soleado": self.soleado
        }

# Ejemplo de uso
if __name__ == "__main__":
    ciudades_predeterminadas = ["Madrid", "Sevilla", "Valencia", "Barcelona", "Asturias", "León"]
    print("Ciudades disponibles:")
    for i, ciudad in enumerate(ciudades_predeterminadas, 1):
        print(f"{i}. {ciudad}")
    
    opcion = int(input("Selecciona una ciudad por su número: "))
    if 1 <= opcion <= len(ciudades_predeterminadas):
        ciudad_seleccionada = ciudades_predeterminadas[opcion - 1]
        tiempo = Tiempo(ciudad_seleccionada)
        datos = tiempo.obtener_datos()
        print(f"Datos meteorológicos para {datos['ciudad']}:")
        print(f"  Temperatura máxima: {datos['temperatura_maxima']}°C")
        print(f"  Temperatura mínima: {datos['temperatura_minima']}°C")
        print(f"  ¿Llueve?: {'Sí' if datos['lluvia'] else 'No'}")
        print(f"  ¿Soleado?: {'Sí' if datos['soleado'] else 'No'}")
    else:
        print("Opción no válida.")