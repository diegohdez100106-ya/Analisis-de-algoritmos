import tkinter as tk

import benchmark as bm
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Comparador de Algoritmos")
root.geometry("600x600")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)


def grafica(N, t_sort, t_bubble, t_insert, t_exchange, t_gnome, t_stooge):
    plt.plot(N, t_sort, marker="o", label="selection")
    plt.plot(N, t_bubble, marker="o", label="bubble")
    plt.plot(N, t_exchange, marker="o", label="excange")
    plt.plot(N, t_gnome, marker="o", label="gnome")
    plt.plot(N, t_insert, marker="o", label="insert")
    plt.plot(N, t_stooge, marker="o", label="stooge")
    plt.ylabel("Tiempo")
    plt.xlabel("tamaños")
    plt.show()

grafica(
    bm.N, bm.t_sort, bm.t_bubble, bm.t_ins, bm.t_exc, bm.t_gno, bm.t_sto
)#print("Lista ordenada:", selection_sort(numeros))
