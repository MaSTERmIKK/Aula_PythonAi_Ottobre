import matplotlib.pyplot as plt
import numpy as np


# grafico a linee

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)

# info extra
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()


# grafico a barre

categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()



data = np.random.randn(1000)

# grafico a istogramma

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show()