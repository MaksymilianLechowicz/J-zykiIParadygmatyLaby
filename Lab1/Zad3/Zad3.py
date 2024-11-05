import numpy as np
ListaNagrody = np.array([10, 5, 7, 15, 13, 2, 6, 1, 3, 17])
ListaCzas = np.array([200, 300, 200, 150, 140, 120, 400, 300, 900, 290])
a = 0
b = 0
c = 0
if len(ListaCzas) == len(ListaNagrody):
    for i in range(len(ListaNagrody)-1):
        for j in range(len(ListaNagrody)-1-i):
            a = ListaCzas[j]/ListaNagrody[j]
            b = ListaCzas[j+1]/ListaNagrody[j+1]
            if a > b:
                c =ListaCzas[j]
                ListaCzas[j] = ListaCzas[j+1]
                ListaCzas[j+1] = c
                c = ListaNagrody[j]
                ListaNagrody[j] = ListaNagrody[j+1]
                ListaNagrody[j+1] = c
print(ListaNagrody,ListaCzas)