from app.tiempo import Tiempo
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_RESULT = ("Consolas", 12)

class TiempoApp:
    def __init__(self, root):
        self.root = root

        self.root.title("🌦️ Tiempo Pro")
        self.root.geometry("480x480")
        self.root.resizable(False, False)

        # Canvas para fondo
        self.canvas = tk.Canvas(root, highlightthickness=0, bg="#f0f4f8")
        self.canvas.pack(fill="both", expand=True)

        # Tarjeta central
        self.card = tk.Frame(root, bg="#ffffff", bd=0, relief="flat")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=600)

        # Título
        self.titulo = tk.Label(self.card, text="Consulta del Clima", font=FONT_TITLE,
                            fg="#222f3e", bg="#ffffff")
        self.titulo.pack(pady=(30, 15))

        # Selector ciudad
        self.lbl_ciudad = tk.Label(self.card, text="Selecciona una ciudad", font=FONT_SUBTITLE,
                            fg="#576574", bg="#ffffff")
        self.lbl_ciudad.pack()
        ciudades = ["Madrid", "Sevilla", "Valencia", "Barcelona", "Asturias", "León"]
        self.combo = ttk.Combobox(self.card, values=ciudades, state="readonly", width=30,
                            font=("Segoe UI", 11))
        self.combo.pack(pady=10)

        # Botón consultar
        self.btn_consultar = tk.Button(self.card, text="Consultar Clima", command=self.mostrar_datos,
                                    bg="#0984e3", fg="#ffffff",
                                    font=("Segoe UI", 11, "bold"), relief="flat",
                                    cursor="hand2", padx=10, pady=7)
        self.btn_consultar.pack(pady=15)

        # Resultado con animación fade-in
        self.resultado = tk.StringVar()
        self.lbl_resultado = tk.Label(self.card, textvariable=self.resultado, font=FONT_RESULT,
                                    fg="#222f3e", bg="#ffffff", justify="left",
                                    wraplength=350)
        self.lbl_resultado.pack(pady=(25, 20))

        # Variables para animar texto
        self.alpha = 0
        self.animar_texto = False

    def mostrar_datos(self):
        ciudad = self.combo.get()
        if ciudad:
            tiempo = Tiempo(ciudad)
            datos = tiempo.obtener_datos()

            # Generar una fecha aleatoria
            dia = random.randint(1, 28)  # Para simplificar, usamos 28 días
            mes = random.randint(1, 12)
            fecha_random = datetime(2025, mes, dia)  # Año fijo para consistencia

            # Llamar al método obtener_estacion desde la instancia
            estacion = tiempo.obtener_estacion(fecha_random)

            icono_lluvia = "🌧️" if datos['lluvia'] else "🌤️"
            icono_sol = "☀️" if datos['soleado'] else "🌥️"

            texto = (
                f"📍 {datos['ciudad']}\n\n"
                f"🌡️ Máxima: {datos['temperatura_maxima']}°C\n"
                f"❄️ Mínima: {datos['temperatura_minima']}°C\n"
                f"{icono_lluvia} ¿Llueve?: {'Sí' if datos['lluvia'] else 'No'}\n"
                f"{icono_sol} ¿Soleado?: {'Sí' if datos['soleado'] else 'No'}\n\n"
                f"📅 Fecha: {fecha_random.strftime('%d/%m/%Y')}\n"
                f"🍂 Estación: {estacion}"
            )

            # Animación fade-in de texto resultado
            self.resultado.set("")
            self.alpha = 0
            self.animar_texto = True
            self.texto_para_animar = texto
            self._fade_in_text()

    def _fade_in_text(self):
        if not self.animar_texto:
            return
        longitud = len(self.texto_para_animar)
        paso = int(longitud * self.alpha / 10)
        self.resultado.set(self.texto_para_animar[:paso])
        self.alpha += 1
        if self.alpha > 10:
            self.animar_texto = False
            self.resultado.set(self.texto_para_animar)
        else:
            self.root.after(40, self._fade_in_text)

def iniciar_app():
    root = tk.Tk()
    app = TiempoApp(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_app()
