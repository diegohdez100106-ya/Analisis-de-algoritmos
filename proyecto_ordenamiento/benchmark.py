import ordenadores as ord
import random
import time

t_sort=[]
t_bubble=[]
t_ins=[]
t_gno=[]
t_exc=[]
t_sto=[]

N=[]

def genera(n, min, max):
    temp=[]
    for i in range(n):
        temp.append(random.randint(min,max))
    return (temp)

listas_n=[]
listas_n2=[]
listas_n3=[]
listas_n4=[]
listas_n5=[]
listas_n6=[]
inicio = 20
fin =101
incremento=20

for i in range(inicio,fin,incremento):
    listas_n.append(genera(i,1,100))
    listas_n2.append(genera(i,1,100))
    listas_n3.append(genera(i,1,100))
    listas_n4.append(genera(i,1,100))
    listas_n5.append(genera(i,1,100))
    listas_n6.append(genera(i,1,100))
    N.append(i)
    print(i)

#genera(20, 1,100)

for i in listas_n:
    t_ini=time.time()
    print(ord.selection_sort(i))
    t_fin=time.time()
    t_sort.append(t_fin-t_ini)
    
for i in listas_n2:
    t_ini=time.time()
    print(ord.bubble_sort_brute_force(i))
    t_fin=time.time()
    t_bubble.append(t_fin-t_ini)
    
for i in listas_n3:
    t_ini=time.time()
    print(ord.insertion_sort(i))
    t_fin=time.time()
    t_ins.append(t_fin-t_ini)

for i in listas_n4:
    t_ini=time.time()
    print (ord.gnome_sort(i))
    t_fin=time.time()
    t_gno.append(t_fin-t_ini)

for i in listas_n5:
    t_ini=time.time()
    print (ord.exchange_sort(i))
    t_fin=time.time()
    t_exc.append(t_fin-t_ini)

for i in listas_n6:
    t_ini=time.time()
    print (ord.stooge_sort(i))
    t_fin=time.time()
    t_sto.append(t_fin-t_ini)
    
print(listas_n)
