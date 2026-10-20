import numpy as np

# 1. Creazione array
array1 = np.arange(0, 50)

casuali = np.random.randint(49, 102, 50)

array1 = np.concatenate((array1, casuali))

print("Array:")
print(array1)

print("Dtype:", array1.dtype)
print("Shape:", array1.shape)


# 2. Conversione in float64
array1 = array1.astype(np.float64)

print("\nNuovo dtype:", array1.dtype)
print("Shape:", array1.shape)


# 3. Slicing

# Primi 10 elementi
primi_10 = array1[:10]

# Ultimi 7 elementi
ultimi_7 = array1[-7:]

# Dall'indice 5 all'indice 20 escluso
da_5_a_20 = array1[5:20]

# Ogni quarto elemento
ogni_quattro = array1[::4]


print("\nPrimi 10:")
print(primi_10)

print("\nUltimi 7:")
print(ultimi_7)

print("\nDa indice 5 a 20:")
print(da_5_a_20)

print("\nOgni quarto elemento:")
print(ogni_quattro)


# 4. Modifica tramite slicing
array1[10:15] = 999

print("\nArray dopo modifica:")
print(array1)


# 5. Fancy indexing

# Posizioni specifiche
posizioni = [0, 3, 7, 12, 25, 33, 48]

elementi_posizioni = array1[posizioni]


# Elementi pari
maschera_pari = array1 % 2 == 0

elementi_pari = array1[maschera_pari]


# Elementi maggiori della media
media = np.mean(array1)

maschera_media = array1 > media

maggiori_media = array1[maschera_media]


# 6. Stampe finali

print("\nArray finale:")
print(array1)

print("\nElementi nelle posizioni richieste:")
print(elementi_posizioni)

print("\nElementi pari:")
print(elementi_pari)

print("\nMedia dell'array:")
print(media)

print("\nElementi maggiori della media:")
print(maggiori_media)