import pandas as pd
from matplotlib import pyplot as plt

lista_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

reta =[]
parabola = []
for i in lista_x:
    reta.append(2*i + 1)
    parabola.append(i**2)


plt.plot(lista_x, reta, label='Reta')
plt.plot(lista_x, parabola, label='Parábola')
plt.legend()
plt.show()