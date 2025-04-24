import tkinter as tk
from tkinter import ttk
from app.tiempo import Tiempo

# 🎨 Paleta de colores
COLOR_BG = "#ecf0f3"
COLOR_TARJETA = "#ffffff"
COLOR_TEXTO = "#2c3e50"
COLOR_TITULO = "#34495e"
COLOR_BOTON = "#3498db"
COLOR_BOTON_TEXTO = "#ffffff"
COLOR_BORDE = "#dcdde1"

def mostrar_datos():
    ciudad = combo_ciudades.get()
    if ciudad:
        clima = Tiempo(ciudad)
        datos = clima.obtener_datos()
        icono_lluvia = "🌧️" if datos['lluvia'] else "🌤️"
        icono_sol = "☀️" if datos['soleado'] else "🌥️"

        resultado.set(
            f"📍 Ciudad: {datos['ciudad']}\n"
            f"{icono_sol} Máxima: {datos['temperatura_maxima']}°C\n"
            f"❄️ Mínima: {datos['temperatura_minima']}°C\n"
            f"{icono_lluvia} ¿Llueve?: {'Sí' if datos['lluvia'] else 'No'}\n"
            f"☀️ ¿Soleado?: {'Sí' if datos['soleado'] else 'No'}"
        )

def iniciar_app():
    global combo_ciudades, resultado

    ventana = tk.Tk()
    ventana.title("🌦️ Tiempo Visual")
    ventana.geometry("450x400")
    ventana.config(bg=COLOR_BG)

    # Título superior
    titulo = tk.Label(ventana, text="Consulta del Clima 🌤️", font=("Helvetica", 18, "bold"), fg=COLOR_TITULO, bg=COLOR_BG)
    titulo.pack(pady=20)

    # Tarjeta principal (como un widget de info)
    tarjeta = tk.LabelFrame(ventana, text="Datos Climáticos", font=("Arial", 12, "bold"), bg=COLOR_TARJETA, bd=2, fg=COLOR_TITULO, labelanchor='n')
    tarjeta.pack(padx=20, pady=10, fill="both", expand=True)

    # Ciudad
    tk.Label(tarjeta, text="Selecciona una ciudad:", bg=COLOR_TARJETA, fg=COLOR_TEXTO, font=("Arial", 10)).pack(pady=(15, 5))
    ciudades = ["Madrid", "Sevilla", "Valencia", "Barcelona", "Asturias", "León"]
    combo_ciudades = ttk.Combobox(tarjeta, values=ciudades, state="readonly", width=30)
    combo_ciudades.pack(pady=5)

    # Botón
    boton = tk.Button(tarjeta, text="🌍 Consultar", command=mostrar_datos,
                    bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO,
                    font=("Arial", 10, "bold"), relief="flat", cursor="hand2")
    boton.pack(pady=15)

    # Resultado visual
    resultado = tk.StringVar()
    resultado_label = tk.Label(tarjeta, textvariable=resultado, bg=COLOR_TARJETA, fg=COLOR_TEXTO,
                        font=("Courier New", 10), justify="left", wraplength=300)
    resultado_label.pack(pady=(5, 20))

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_app()

