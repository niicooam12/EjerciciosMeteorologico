import tkinter as tk
from tkinter import ttk
from tiempo import Tiempo

def mostrar_datos():
    ciudad = combo_ciudades.get()
    if ciudad:
        clima = Tiempo(ciudad)
        datos = clima.obtener_datos()
        resultado.set(
            f"Ciudad: {datos['ciudad']}\n"
            f"Temperatura Máxima: {datos['temperatura_maxima']}°C\n"
            f"Temperatura Mínima: {datos['temperatura_minima']}°C\n"
            f"¿Llueve?: {'Sí' if datos['lluvia'] else 'No'}\n"
            f"¿Soleado?: {'Sí' if datos['soleado'] else 'No'}"
        )

# Ventana principal
ventana = tk.Tk()
ventana.title("Consulta del Tiempo")
ventana.geometry("350x250")

# Lista de ciudades
ciudades = ["Madrid", "Sevilla", "Valencia", "Barcelona", "Asturias", "León"]

# Combobox para seleccionar ciudad
tk.Label(ventana, text="Selecciona una ciudad:").pack(pady=10)
combo_ciudades = ttk.Combobox(ventana, values=ciudades, state="readonly")
combo_ciudades.pack()

# Botón para consultar
tk.Button(ventana, text="Consultar Tiempo", command=mostrar_datos).pack(pady=10)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado, justify="left", font=("Arial", 10)).pack(pady=10)

ventana.mainloop()

def iniciar_app():
    ventana.mainloop()

if __name__ == "__main__":
    iniciar_app()

