import tkinter as tk
import benchmark as bm
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Comparador de Algoritmos")
root.geometry("600x600")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

title_lbl = tk.Label(
    frame,
    text="Generador de Arreglos Ordenados",
)
title_lbl.grid(row=0, column=0, columnspan=2, pady=15, padx=5)

lbl_start = tk.Label(
    frame,
    text="Arreglo Inicial: ",
    anchor="w",
    width=15,
)
lbl_start.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_start = tk.Entry(frame)
entry_start.grid(row=1, column=1, padx=10, pady=5, sticky="w")

lbl_increment = tk.Label(frame, text="Incremento:", anchor="w", width=15)
lbl_increment.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_inc = tk.Entry(frame)
entry_inc.grid(row=2, column=1, padx=10, pady=5, sticky="w")

lbl_limit = tk.Label(frame, text="Limite:", anchor="w", width=15)
lbl_limit.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_limit = tk.Entry(frame)
entry_limit.grid(row=3, column=1, padx=10, pady=5, sticky="w")


def ordenar_arreglos():
    ini = int(entry_start.get())
    inc = int(entry_inc.get())
    lim = int(entry_limit.get())
    if ini or inc or lim != None:
        bm.ordena(ini, lim, inc)
    else:
        return
    grafica(
        bm.N,
        bm.t_sort,
        bm.t_bubble,
        bm.t_ins,
        bm.t_exc,
        bm.t_gno,
        bm.t_merge,
        bm.t_quick,
    )


btn_generator = tk.Button(frame, text="Ordenar Arreglos", command=ordenar_arreglos)
btn_generator.grid(row=4, column=0, columnspan=2, padx=5, pady=15, sticky="w")


def grafica(N, t_sort, t_bubble, t_insert, t_exchange, t_gnome, t_merge, t_quick):
    plt.plot(N, t_sort, marker="o", label="Selection")
    plt.plot(N, t_bubble, marker="o", label="Bubble")
    plt.plot(N, t_insert, marker="o", label="Insert")
    plt.plot(N, t_exchange, marker="o", label="Exchange")
    plt.plot(N, t_gnome, marker="o", label="Gnome")
    plt.plot(N, t_merge, marker="o", label="Merge")
    plt.plot(N, t_quick, marker="o", label="Quick")
    plt.ylabel("Tiempo (s)")
    plt.xlabel("Tamaño del arreglo")
    plt.legend()
    plt.show()


root.mainloop()