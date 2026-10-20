import numpy as np

# ==========================================
# ESEMPIO 1 - Broadcasting con uno scalare
# ==========================================

numeri = np.array([10, 20, 30, 40])

risultato = numeri * 2

print("ESEMPIO 1:")
print(risultato)
# [20 40 60 80]


# ==========================================
# ESEMPIO 2 - Somma tra matrice e vettore
# ==========================================

matrice = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vettore = np.array([10, 20, 30])

risultato = matrice + vettore

print("\nESEMPIO 2:")
print(risultato)
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]


# ==========================================
# ESEMPIO 3 - Broadcasting per righe
# ==========================================

matrice = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

colonna = np.array([
    [10],
    [20],
    [30]
])

risultato = matrice + colonna

print("\nESEMPIO 3:")
print(risultato)
# [[11 12 13]
#  [24 25 26]
#  [37 38 39]]


# ==========================================
# ESEMPIO 4 - Broadcasting con reshape()
# ==========================================

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Trasformiamo il vettore in una colonna
a = a.reshape(3, 1)

risultato = a + b

print("\nESEMPIO 4:")
print(risultato)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]


# ==========================================
# ESEMPIO 5 - Aumento dei prezzi
# ==========================================

prezzi = np.array([100, 200, 300, 400])

aumento = 0.10

# Applichiamo il 10% a tutti i prezzi
nuovi_prezzi = prezzi * (1 + aumento)

print("\nESEMPIO 5:")
print(nuovi_prezzi)
# [110. 220. 330. 440.]


# ==========================================
# ESEMPIO 6 - Sconti differenti
# ==========================================

prezzi = np.array([100, 200, 300])

sconti = np.array([
    [0.10],
    [0.20],
    [0.30]
])

# Ogni sconto viene applicato a tutti i prodotti
risultato = prezzi * (1 - sconti)

print("\nESEMPIO 6:")
print(risultato)
# [[ 90. 180. 270.]
#  [ 80. 160. 240.]
#  [ 70. 140. 210.]]


# ==========================================
# ESEMPIO 7 - Broadcasting non compatibile
# ==========================================

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20])

print("\nESEMPIO 7:")

try:
    risultato = a + b
    print(risultato)

except ValueError:
    print("Errore: dimensioni non compatibili!")
    print("Shape A:", a.shape)
    print("Shape B:", b.shape)
