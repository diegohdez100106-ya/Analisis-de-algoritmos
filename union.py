import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time
import random

def bubble_sort(arr):
    time_in=time.time()
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    time_f=time.time()
    timepos=time_f-time_in
    return timepos

def selection_sort(arr):
    time_in=time.time()
    data = arr.copy()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    time_f=time.time()
    tiempos=time_f-time_in
    return tiempos


def generar_y_graficar():
        inicio = int(entry_inicio.get().strip())
        paso = int(entry_paso.get().strip())
        tope = int(entry_tope.get().strip())

        if paso <= 0 or inicio > tope:
            lbl_resultado.config(text="Error: Revisa los rangos (Inicio <= Tope y Paso > 0).")
            return

        tamanos = list(range(inicio, tope + 1, paso))
        tiempos_bubble = []
        tiempos_selection = []

        texto_resultado = f"Se procesaron {len(tamanos)} arreglos:\n\n"
        for n in tamanos:
            arr_original = [random.randint(1, 1000) for _ in range(n)]

            tmpbubble = bubble_sort(arr_original)
            tiempos_bubble.append(tmpbubble)

            tmpselect = selection_sort(arr_original)
            tiempos_selection.append(tmpselect)


        lbl_resultado.config(text=texto_resultado)
        print(texto_resultado)

        plt.figure()
        plt.plot(tamanos, tiempos_bubble, label='Bubble Sort', color='#FF5733')
        plt.plot(tamanos, tiempos_selection, label='Selection Sort', color='#33FF57')

        plt.xlabel('Tamaño del Arreglo (N)')
        plt.ylabel('Tiempo de Ejecución (segundos)')
        plt.title('Comparativa: Bubble Sort vs Selection Sort')
        plt.legend()
        plt.show()


root = tk.Tk()
root.title("Comparador de Ordenamiento")
root.geometry("450x450")

tk.Label(root, text="Valor Inicial").pack(pady=(10, 0))
entry_inicio = tk.Entry(root)
entry_inicio.pack()

tk.Label(root, text="Paso / Incremento").pack(pady=(5, 0))
entry_paso = tk.Entry(root)
entry_paso.pack()

tk.Label(root, text="Tope Máximo").pack(pady=(5, 0))
entry_tope = tk.Entry(root)
entry_tope.pack()

btn_procesar = tk.Button(root, text="Generar y Graficar", command=generar_y_graficar)
btn_procesar.pack(pady=10)

lbl_resultado = tk.Label(root, text="", wraplength=420, justify="left")
lbl_resultado.pack(pady=5)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()