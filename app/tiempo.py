import random

class Tiempo:
    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.generar_datos_climaticos()

    def generar_datos_climaticos(self):
        self.temperatura_maxima = random.randint(20, 40)
        self.temperatura_minima = random.randint(0, self.temperatura_maxima - 1)

        # Aseguramos coherencia: no puede llover y estar completamente soleado al mismo tiempo
        self.lluvia = random.choice([True, False])
        self.soleado = not self.lluvia if random.random() < 0.7 else random.choice([True, False])

    def obtener_datos(self):
        return {
            "ciudad": self.ciudad,
            "temperatura_maxima": self.temperatura_maxima,
            "temperatura_minima": self.temperatura_minima,
            "lluvia": self.lluvia,
            "soleado": self.soleado
        }
