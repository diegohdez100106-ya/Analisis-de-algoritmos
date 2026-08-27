import tkinter as tk
import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot as plt

x = [3]
y=[10]

plt.plot(x,y)
plt.title("mi primer grafica")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.show()

def saludar():
    nombre = entry.get().strip()
    if not nombre:
        nombre = "Diego Hernandez"
    lbl.config(text = f"hola {nombre}, pucheo confirmed")

root = tk.Tk()
root.title ("saludador")
root.geometry ("360x220")

lbl = tk.Label (root, text="Escribe tu nombre y presion el boton", foreground="white")
lbl.pack(pady=20)

entry=tk.Entry(root, background="grey")
entry.pack(pady=10)

button = tk.Button (root, text="puchame", command=saludar)
button.pack()
root.mainloop()
