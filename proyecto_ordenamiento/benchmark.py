import random
import time
import ordenadores as ord

t_sort = []
t_bubble = []
t_ins = []
t_gno = []
t_exc = []
t_merge = []
t_quick = []

N = []


def genera(n, min, max):
    temp = []
    for i in range(n):
        temp.append(random.randint(min, max))
    return temp


def ordena(ini, fin, inc):
    listas_n = []
    listas_n2 = []
    listas_n3 = []
    listas_n4 = []
    listas_n5 = []
    listas_n6 = []
    listas_n7 = []

    for i in range(ini, fin, inc):
        listas_n.append(genera(i, 1, 100))
        listas_n2.append(genera(i, 1, 100))
        listas_n3.append(genera(i, 1, 100))
        listas_n4.append(genera(i, 1, 100))
        listas_n5.append(genera(i, 1, 100))
        listas_n6.append(genera(i, 1, 100))
        listas_n7.append(genera(i, 1, 100))
        N.append(i)
        print(i)

    # genera(20, 1,100)

    for i in listas_n:
        t_ini = time.time()
        print(ord.selection_sort(i))
        t_fin = time.time()
        t_sort.append(t_fin - t_ini)

    for i in listas_n2:
        t_ini = time.time()
        print(ord.bubble_sort_brute_force(i))
        t_fin = time.time()
        t_bubble.append(t_fin - t_ini)

    for i in listas_n3:
        t_ini = time.time()
        print(ord.insertion_sort(i))
        t_fin = time.time()
        t_ins.append(t_fin - t_ini)

    for i in listas_n4:
        t_ini = time.time()
        print(ord.gnome_sort(i))
        t_fin = time.time()
        t_gno.append(t_fin - t_ini)

    for i in listas_n5:
        t_ini = time.time()
        print(ord.exchange_sort(i))
        t_fin = time.time()
        t_exc.append(t_fin - t_ini)

    for i in listas_n6:
        t_ini = time.time()
        print(ord.merge_sort(i))
        t_fin = time.time()
        t_merge.append(t_fin - t_ini)

    for i in listas_n7:
        t_ini = time.time()
        print(ord.quick_sort(i))
        t_fin = time.time()
        t_quick.append(t_fin - t_ini)

    print(listas_n)