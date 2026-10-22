
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. GENERAZIONE DEI DATI

# Generiamo 365 giorni di visitatori
np.random.seed(42)

visitatori = np.random.normal(2000, 500, 365)

# Convertiamo i valori in interi ed evitiamo numeri negativi
visitatori = np.maximum(visitatori.astype(int), 0)

# 2. CREAZIONE DEL DATAFRAME

# Creiamo le date per 365 giorni
date = pd.date_range(start="2026-01-01", periods=365)

# Creiamo il DataFrame con le date come indice
df = pd.DataFrame({
    "Visitatori": visitatori
}, index=date)

print("PRIMI 5 GIORNI")
print(df.head())

# 3. ANALISI DEI DATI

# Calcoliamo la media mensile
media_mensile = df.resample("MS").mean()

# Calcoliamo la deviazione standard
deviazione = df["Visitatori"].std()

print("\nMEDIA MENSILE")
print(media_mensile)

print("\nDEVIAZIONE STANDARD")
print(deviazione)

# 4. MEDIA MOBILE A 7 GIORNI

# Calcoliamo la media degli ultimi 7 giorni
df["MediaMobile"] = df["Visitatori"].rolling(7).mean()

# 5. PRIMO GRAFICO: VISITATORI GIORNALIERI

plt.figure(figsize=(12, 5))

plt.plot(df.index, df["Visitatori"], label="Visitatori")

plt.plot(df.index, df["MediaMobile"],
         label="Media mobile 7 giorni", color="red")

plt.title("Visitatori giornalieri")
plt.xlabel("Data")
plt.ylabel("Numero visitatori")
plt.legend()
plt.grid(True)
plt.show()

# 6. SECONDO GRAFICO: MEDIA MENSILE

plt.figure(figsize=(10, 5))

plt.bar(media_mensile.index.month,
        media_mensile["Visitatori"])

plt.title("Media mensile dei visitatori")
plt.xlabel("Mese")
plt.ylabel("Media visitatori")
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()
