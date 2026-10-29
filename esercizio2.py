import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Simuliamo i risultati: 1 = vittoria, 0 = sconfitta
np.random.seed(42)
risultati = np.random.choice([0, 1], size=20, p=[0.4, 0.6])

# Creiamo le giornate da 1 a 20
giornate = np.arange(1, 21)


# Troviamo la serie più lunga di vittorie consecutive

# Lista che conterrà la lunghezza di ogni serie
serie = []

# Contatore delle vittorie consecutive attuali
corrente = 0

# Esaminiamo ogni risultato
for r in risultati:
    if r == 1:
        # Se è una vittoria, aumentiamo il contatore
        corrente += 1
    else:
        # Se è una sconfitta, salviamo la serie terminata
        serie.append(corrente)

        # Azzeriamo il contatore per la serie successiva
        corrente = 0

# Salviamo anche l'eventuale ultima serie di vittorie
serie.append(corrente)

# Troviamo il numero massimo di vittorie consecutive
serie_max = max(serie)


# Troviamo dove si trova la serie più lunga

# Creiamo una sequenza di 1 lunga quanto la serie massima
# Esempio: se serie_max = 3, otteniamo [1, 1, 1]
sequenza = np.ones(serie_max, dtype=int)

# Calcoliamo le somme di tutti i gruppi consecutivi
# della stessa lunghezza della serie massima
somme = np.convolve(risultati, sequenza, 'valid')

# Troviamo il primo gruppo la cui somma equivale
# alla lunghezza massima: tutti i risultati sono vittorie
indice_inizio = np.where(somme == serie_max)[0][0]

# Troviamo la giornata finale della serie
fine_serie = indice_inizio + serie_max

# Troviamo la giornata iniziale della serie
inizio_serie = fine_serie - serie_max + 1


# Creiamo il grafico
plt.figure(figsize=(9, 5))

# Disegniamo i risultati con una linea a gradini
plt.plot(
    giornate, risultati,
    drawstyle='steps-mid',
    color='gray',
    lw=2
)

# Evidenziamo le vittorie con marker verdi
plt.scatter(
    giornate[risultati == 1],
    risultati[risultati == 1],
    color='green',
    s=100,
    label='Vittoria'
)

# Evidenziamo le sconfitte con marker rossi
plt.scatter(
    giornate[risultati == 0],
    risultati[risultati == 0],
    color='red',
    s=100,
    label='Sconfitta'
)


# Evidenziamo la serie più lunga con una fascia verde
plt.axvspan(
    inizio_serie, fine_serie,
    color='lime',
    alpha=0.2,
    label='Serie più lunga'
)


# Aggiungiamo una freccia e un'annotazione sulla serie
plt.annotate(
    f"Serie di {serie_max} vittorie",
    xy=(fine_serie, 1),
    xytext=(fine_serie - 4, 1.3),
    arrowprops=dict(facecolor='green', arrowstyle='->'),
    fontsize=10,
    color='green'
)


# Personalizziamo il grafico
plt.title("Serie Sportiva – Vittorie Evidenziate")
plt.xlabel("Giornata")
plt.ylabel("Risultato (1=Vittoria, 0=Sconfitta)")

# Impostiamo i limiti dell'asse verticale
plt.ylim(-0.2, 1.5)

# Attiviamo la griglia tratteggiata e semitrasparente
plt.grid(True, linestyle='--', alpha=0.5)

# Mostriamo la legenda
plt.legend()

# Sistemiamo gli spazi del grafico
plt.tight_layout()

# Visualizziamo il grafico
plt.show()