def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort_brute_force(lista):
    arr = lista.copy()
    n = len(arr)
    # Ciclo externo corre n veces de forma fija
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(lista):
    """
    Ordenamiento por Inserción.
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        # Compara la clave con los elementos anteriores y los desplaza
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr


def gnome_sort(lista):
    arr = lista.copy()
    i = 0
    n = len(arr)

    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1  # Avanza si está en orden
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Intercambia
            i -= 1  # Retrocede un paso

    return arr


def exchange_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Si el elemento posterior es menor, intercambia de inmediato
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def merge_sort(lista):
    arr = lista.copy()

    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(arr) <= 1:
        return

    # 1. DIVIDE: Encontrar el punto medio y dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. VENCE: Llamadas recursivas para ordenar cada mitad
    merge_sort(left_half)
    merge_sort(right_half)

    # 3. COMBINA (Merge): Fusionar las dos mitades ordenadas en la lista original
    i = j = k = 0

    # Comparar elementos de ambas mitades y colocar el menor en 'arr'
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Verificar si quedaron elementos en la mitad izquierda
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Verificar si quedaron elementos en la mitad derecha
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return arr


def quick_sort(lista):
    arr = lista.copy()

    # Caso base: una lista vacía o con un solo elemento ya está ordenada
    if len(arr) <= 1:
        return arr

    # Elección del pivote (en este caso, el elemento central)
    pivot = arr[len(arr) // 2]

    # Particionamiento de la lista
    izq = [x for x in arr if x < pivot]
    centro = [x for x in arr if x == pivot]
    der = [x for x in arr if x > pivot]

    # Llamada recursiva combinando los resultados
    return quick_sort(izq) + centro + quick_sort(der)