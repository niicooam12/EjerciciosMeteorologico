from app.tiempo import Tiempo
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

MODOS = {
    "claro": {
        "bg": "#f0f4f8",
        "card_bg": "#ffffff",
        "text": "#222f3e",
        "subtext": "#576574",
        "accent": "#0984e3",
        "boton_bg": "#0984e3",
        "boton_fg": "#ffffff"
    },
    "oscuro": {
        "bg": "#121418",
        "card_bg": "#1e272e",
        "text": "#d2dae2",
        "subtext": "#8395a7",
        "accent": "#00cec9",
        "boton_bg": "#00cec9",
        "boton_fg": "#121418"
    }
}

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_RESULT = ("Consolas", 12)

class TiempoApp:
    def __init__(self, root):
        self.root = root
        self.modo = "claro"
        self.config = MODOS[self.modo]

        self.root.title("🌦️ Tiempo Pro")
        self.root.geometry("480x480")
        self.root.resizable(False, False)

        # Canvas para fondo con gradiente simple simulado
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.dibujar_fondo()

        # Tarjeta central
        self.card = tk.Frame(root, bg=self.config["card_bg"], bd=0, relief="flat")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=600)

        # Título
        self.titulo = tk.Label(self.card, text="Consulta del Clima", font=FONT_TITLE,
                            fg=self.config["text"], bg=self.config["card_bg"])
        self.titulo.pack(pady=(30, 15))

        # Selector ciudad
        self.lbl_ciudad = tk.Label(self.card, text="Selecciona una ciudad", font=FONT_SUBTITLE,
                            fg=self.config["subtext"], bg=self.config["card_bg"])
        self.lbl_ciudad.pack()
        ciudades = ["Madrid", "Sevilla", "Valencia", "Barcelona", "Asturias", "León"]
        self.combo = ttk.Combobox(self.card, values=ciudades, state="readonly", width=30,
                            font=("Segoe UI", 11))
        self.combo.pack(pady=10)

        # Botones consultar y toggle modo
        self.btn_consultar = tk.Button(self.card, text="Consultar Clima", command=self.mostrar_datos,
                                    bg=self.config["boton_bg"], fg=self.config["boton_fg"],
                                    font=("Segoe UI", 11, "bold"), relief="flat",
                                    cursor="hand2", padx=10, pady=7)
        self.btn_consultar.pack(pady=15)

        self.btn_toggle = tk.Button(self.card, text="Modo Oscuro 🌙", command=self.toggle_modo,
                                    bg=self.config["boton_bg"], fg=self.config["boton_fg"],
                                    font=("Segoe UI", 10), relief="flat",
                                    cursor="hand2", padx=8, pady=5)
        self.btn_toggle.pack()

        # Resultado con animación fade-in
        self.resultado = tk.StringVar()
        self.lbl_resultado = tk.Label(self.card, textvariable=self.resultado, font=FONT_RESULT,
                                    fg=self.config["text"], bg=self.config["card_bg"], justify="left",
                                    wraplength=350)
        self.lbl_resultado.pack(pady=(25, 20))

        # Variables para animar texto
        self.alpha = 0
        self.animar_texto = False

    def dibujar_fondo(self):
        """Simula un fondo degradado vertical en el canvas"""
        self.canvas.delete("all")
        w = 480
        h = 480
        r1, g1, b1 = self.hex_a_rgb(self.config["bg"])
        r2, g2, b2 = (255, 255, 255) if self.modo == "claro" else (30, 39, 46)
        pasos = 100
        for i in range(pasos):
            r = int(r1 + (r2 - r1) * i / pasos)
            g = int(g1 + (g2 - g1) * i / pasos)
            b = int(b1 + (b2 - b1) * i / pasos)
            color = f"#{r:02x}{g:02x}{b:02x}"
            y1 = int(h * i / pasos)
            y2 = int(h * (i + 1) / pasos)
            self.canvas.create_rectangle(0, y1, w, y2, outline="", fill=color)

    def hex_a_rgb(self, hex_color):
        """Convierte #rrggbb a (r, g, b)"""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def toggle_modo(self):
        """Cambia modo claro/oscuro con animación de fondo y colores"""
        self.modo = "oscuro" if self.modo == "claro" else "claro"
        self.config = MODOS[self.modo]
        self.dibujar_fondo()

        # Cambia colores
        self.card.config(bg=self.config["card_bg"])
        self.titulo.config(fg=self.config["text"], bg=self.config["card_bg"])
        self.lbl_ciudad.config(fg=self.config["subtext"], bg=self.config["card_bg"])
        self.btn_consultar.config(bg=self.config["boton_bg"], fg=self.config["boton_fg"])
        self.btn_toggle.config(bg=self.config["boton_bg"], fg=self.config["boton_fg"])
        self.lbl_resultado.config(fg=self.config["text"], bg=self.config["card_bg"])

        # Cambia texto botón toggle
        texto = "Modo Claro ☀️" if self.modo == "oscuro" else "Modo Oscuro 🌙"
        self.btn_toggle.config(text=texto)

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