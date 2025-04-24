import tkinter as tk
from tkinter import ttk
from app.tiempo import Tiempo

COLOR_BG = "#eaf0f6"
COLOR_CARD = "#ffffff"
COLOR_ACCENT = "#4a90e2"
COLOR_TEXT = "#2d3436"
COLOR_SUBTEXT = "#636e72"
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_SUBTITLE = ("Segoe UI", 10)
FONT_RESULT = ("Consolas", 11)

def mostrar_datos():
    ciudad = combo.get()
    if ciudad:
        tiempo = Tiempo(ciudad)
        datos = tiempo.obtener_datos()

        icono_lluvia = "🌧️" if datos['lluvia'] else "🌤️"
        icono_sol = "☀️" if datos['soleado'] else "🌥️"

        resultado.set(
            f"📍 {datos['ciudad']}\n\n"
            f"🌡️ Máxima: {datos['temperatura_maxima']}°C\n"
            f"❄️ Mínima: {datos['temperatura_minima']}°C\n"
            f"{icono_lluvia} ¿Llueve?: {'Sí' if datos['lluvia'] else 'No'}\n"
            f"{icono_sol} ¿Soleado?: {'Sí' if datos['soleado'] else 'No'}"
        )

def iniciar_app():
    global combo, resultado

    ventana = tk.Tk()
    ventana.title("🌦️ Tiempo App")
    ventana.geometry("440x420")
    ventana.configure(bg=COLOR_BG)
    ventana.resizable(False, False)

    # Card principal
    card = tk.Frame(ventana, bg=COLOR_CARD, bd=0, relief="flat")
    card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=360)

    # Título
    tk.Label(card, text="Consulta del Clima", font=FONT_TITLE, fg=COLOR_TEXT, bg=COLOR_CARD).pack(pady=(20, 10))

    # Selector ciudad
    tk.Label(card, text="Selecciona una ciudad", font=FONT_SUBTITLE, fg=COLOR_SUBTEXT, bg=COLOR_CARD).pack()
    ciudades = ["Madrid", "Sevilla", "Valencia", "Barcelona", "Asturias", "León"]
    combo = ttk.Combobox(card, values=ciudades, state="readonly", width=28, font=("Segoe UI", 10))
    combo.pack(pady=5)

    # Botón consultar
    boton = tk.Button(card, text="Consultar Clima", command=mostrar_datos,
                      bg=COLOR_ACCENT, fg="white", activebackground="#3b7bd5",
                      font=("Segoe UI", 10, "bold"), relief="flat", cursor="hand2", padx=10, pady=5)
    boton.pack(pady=20)

    # Resultado
    resultado = tk.StringVar()
    resultado_label = tk.Label(card, textvariable=resultado, font=FONT_RESULT, fg=COLOR_TEXT, bg=COLOR_CARD, justify="left")
    resultado_label.pack(pady=(5, 10))

    ventana.mainloop()


if __name__ == "__main__":
    iniciar_app()

