import random
from datetime import datetime

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

    def obtener_estacion(self, fecha):
        """
        Determina la estación del año según la fecha proporcionada.
        """
        dia, mes = fecha.day, fecha.month
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
            return "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
            return "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 21):
            return "Invierno"
        elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
            return "Primavera"