
# Importiamo le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Fissiamo il seme per ottenere sempre gli stessi numeri casuali
np.random.seed(42)

# Creiamo 12 date settimanali a partire dal 1° gennaio 2025
settimane = pd.date_range("2025-01-01", freq="W", periods=12)

# Generiamo 12 valori di vendita casuali tra 200 e 799 euro
vendite = np.random.randint(200, 800, size=12)

# Troviamo la posizione del valore massimo
idx_max = np.argmax(vendite)

# Recuperiamo il valore massimo delle vendite
val_max = vendite[idx_max]

# Creiamo una figura di dimensioni 8 x 5 pollici
plt.figure(figsize=(8, 5))

# Disegniamo il grafico a linee con punti circolari blu
plt.plot(
    settimane, vendite,
    color="royalblue",
    marker="o",
    linewidth=2
)

# Impostiamo il titolo del grafico
plt.title("Vendite Settimanali con Annotazione del Massimo")

# Etichettiamo gli assi
plt.xlabel("Settimana")
plt.ylabel("Vendite (€)")

# Attiviamo la griglia tratteggiata, completamente visibile
plt.grid(True, linestyle="--", alpha=1)

# Evidenziamo il massimo con un punto rosso
plt.scatter(
    settimane[idx_max], val_max,
    color="red",
    s=100,
    zorder=5,
    label="Massimo"
)

# Aggiungiamo una scritta e una freccia sul valore massimo
plt.annotate(
    f"Massimo: {val_max}€",
    xy=(settimane[idx_max], val_max),
    xytext=(settimane[idx_max], val_max + 65),
    arrowprops=dict(facecolor="red", arrowstyle="->"),
    ha="center",
    color="red"
)

# Mostriamo la legenda
plt.legend()

# Sistemiamo automaticamente gli spazi della figura
plt.tight_layout()

# Visualizziamo il grafico
plt.show()
