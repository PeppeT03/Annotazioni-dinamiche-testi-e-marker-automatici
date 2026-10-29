import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(42)

date = pd.date_range("01-01-2025", periods=60)

prezzi = 100 + np.cumsum(np.random.randn(60))

iniziale = prezzi[0]

variazioni = prezzi - iniziale

ultimo_valore = prezzi[-1]

plt.figure(figsize=(10,6))

plt.plot(date,prezzi,color="steelblue",label="Prezzo",linewidth=2)
plt.fill_between(date,prezzi,iniziale,where=(prezzi>=iniziale),color="green",alpha=0.2,label="Zona di guadagno")
plt.fill_between(date,prezzi,iniziale,where=(prezzi<iniziale),color="red",alpha=0.2,label="Zona di perdita")
plt.scatter(date[-1],ultimo_valore,color="black",s=100)
plt.annotate(f"Valore attuale: {ultimo_valore:.2f}",xy=(date[-1], ultimo_valore),xytext=(date[-15], ultimo_valore + 3),arrowprops=dict(color="black",arrowstyle='->'))
plt.text(x=date[5],y=iniziale+4,s="Zona di guadagno",color="green",fontsize=10)
plt.text(x=date[30],y=iniziale-4,s="Zona di perdita",color="red",fontsize=10)
plt.title("Andamento Finanziario con Zone di Guadagno e Perdita")
plt.xlabel("Data")
plt.ylabel("Prezzo (€)")
plt.grid(True, linestyle="--", alpha=0.5)


plt.legend()
plt.tight_layout()
plt.show()

