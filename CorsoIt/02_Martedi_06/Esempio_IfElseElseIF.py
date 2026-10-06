"""
CONDIZIONI IN PYTHON

- if
- else
- elif
- operatori di confronto
- and
- or
- not
- condizioni annidate
- operatore ternario

NOTA:
In Python non esiste "else if".
Si utilizza la parola chiave "elif".
"""


# ==============================================================
# 1. IF BASE
# ==============================================================

eta = 20

if eta >= 18:
    print("Sei maggiorenne")

print()


# ==============================================================
# 2. IF - ELSE
# ==============================================================

eta = 16

if eta >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

print()


# ==============================================================
# 3. IF - ELIF - ELSE
# ==============================================================

voto = 25

if voto >= 28:
    print("Ottimo")
elif voto >= 24:
    print("Buono")
elif voto >= 18:
    print("Sufficiente")
else:
    print("Insufficiente")

print()


# ==============================================================
# 4. OPERATORI DI CONFRONTO
# ==============================================================

a = 10
b = 20

print(a == b)   # Uguale
print(a != b)   # Diverso
print(a > b)    # Maggiore
print(a < b)    # Minore
print(a >= b)   # Maggiore o uguale
print(a <= b)   # Minore o uguale

print()


# ==============================================================
# 5. IF CON UGUAGLIANZA
# ==============================================================

password = "python123"

if password == "python123":
    print("Password corretta")
else:
    print("Password errata")

print()


# ==============================================================
# 6. AND
# Entrambe le condizioni devono essere vere
# ==============================================================

eta = 25
patente = True

if eta >= 18 and patente:
    print("Puoi guidare")
else:
    print("Non puoi guidare")

print()


# ==============================================================
# 7. OR
# Basta che una delle condizioni sia vera
# ==============================================================

giorno = "sabato"

if giorno == "sabato" or giorno == "domenica":
    print("È weekend")
else:
    print("È un giorno lavorativo")

print()


# ==============================================================
# 8. NOT
# Inverte il valore logico
# ==============================================================

utente_bloccato = False

if not utente_bloccato:
    print("Accesso consentito")
else:
    print("Accesso negato")

print()


# ==============================================================
# 9. PIÙ ELIF
# ==============================================================

temperatura = 24

if temperatura >= 35:
    print("Molto caldo")

elif temperatura >= 25:
    print("Caldo")

elif temperatura >= 15:
    print("Temperatura mite")

elif temperatura >= 5:
    print("Freddo")

else:
    print("Molto freddo")

print()


# ==============================================================
# 10. CONDIZIONI ANNIDATE
# ==============================================================

eta = 25
patente = True

if eta >= 18:

    print("Sei maggiorenne")

    if patente:
        print("Puoi guidare")
    else:
        print("Non hai la patente")

else:
    print("Sei minorenne")

print()


# ==============================================================
# 11. CONTROLLO DI UN INTERVALLO
# ==============================================================

numero = 15

if numero >= 10 and numero <= 20:
    print("Il numero è compreso tra 10 e 20")
else:
    print("Il numero è fuori dall'intervallo")

print()


# ==============================================================
# 12. FORMA COMPATTA PER GLI INTERVALLI
# ==============================================================

numero = 15

if 10 <= numero <= 20:
    print("Numero valido")

print()


# ==============================================================
# 13. CONTROLLO NUMERO POSITIVO, NEGATIVO O ZERO
# ==============================================================

numero = -5

if numero > 0:
    print("Positivo")

elif numero < 0:
    print("Negativo")

else:
    print("Zero")

print()


# ==============================================================
# 14. PARI O DISPARI
# ==============================================================

numero = 7

if numero % 2 == 0:
    print("Numero pari")
else:
    print("Numero dispari")

print()


# ==============================================================
# 15. IF CON STRINGHE
# ==============================================================

ruolo = "admin"

if ruolo == "admin":
    print("Accesso amministratore")

elif ruolo == "utente":
    print("Accesso utente")

elif ruolo == "ospite":
    print("Accesso limitato")

else:
    print("Ruolo sconosciuto")

print()


# ==============================================================
# 16. IF CON LISTE E IN
# ==============================================================

utenti = ["Mario", "Anna", "Luca"]

nome = "Anna"

if nome in utenti:
    print(nome, "è presente")
else:
    print(nome, "non è presente")

print()


# ==============================================================
# 17. IF CON NOT IN
# ==============================================================

nome = "Marco"

if nome not in utenti:
    print(nome, "non è registrato")

print()


# ==============================================================
# 18. IF CON BOOLEANI
# ==============================================================

online = True

if online:
    print("Utente online")
else:
    print("Utente offline")

print()


# ==============================================================
# 19. OPERATORE TERNARIO
# IF - ELSE IN UNA SOLA RIGA
# ==============================================================

eta = 20

messaggio = "Maggiorenne" if eta >= 18 else "Minorenne"

print(messaggio)

print()


# ==============================================================
# 20. ESEMPIO PRATICO: LOGIN
# ==============================================================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login effettuato")

elif username == "admin":
    print("Password errata")

else:
    print("Utente non trovato")

print()


# ==============================================================
# 21. ESEMPIO PRATICO: VALUTAZIONE VOTO
# ==============================================================

voto = 27

if voto < 0 or voto > 30:
    print("Voto non valido")

elif voto >= 28:
    print("Ottimo")

elif voto >= 24:
    print("Buono")

elif voto >= 18:
    print("Sufficiente")

else:
    print("Insufficiente")
