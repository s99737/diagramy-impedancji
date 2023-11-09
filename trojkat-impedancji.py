import math

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

# Dane impedancji
Z_ohms = 231.17
R_ohms = 119.40
phi_deg = 58.90
negative = False
title = "Trójkąt impedancji dla pomiaru Z1 nr 1"

# Oblicz X
X_ohms = round(math.sqrt(Z_ohms ** 2 - R_ohms ** 2), 2)

# Konwersja kąta ze stopni na radiany
phi_rad = np.deg2rad(phi_deg)

# Utwórz nowy wykres
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')

# Utwórz siatkę
ax.grid(which="both", linestyle="-", linewidth=0.5)

# Narysuj trójkąt impedancji
ax.plot([0, R_ohms], [0, 0], 'r')
ax.plot([R_ohms, R_ohms], [0, X_ohms], 'b')
ax.plot([0, R_ohms], [0, X_ohms], 'g')

# Dodaj kąt między R i Z
angle = Wedge(center=(0, 0), r=(R_ohms / 4), theta1=0, theta2=phi_deg, color='black', alpha=0.2)
ax.add_patch(angle)

# Dodaj adnotacje nad przyprostokątnymi
ax.annotate(f"R = {R_ohms} Ω", (R_ohms / 2, 0), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=12)
ax.annotate(f"X = {X_ohms} Ω", (R_ohms, X_ohms / 2), textcoords="offset points", xytext=(10, 0), va='center', fontsize=12, rotation=-90)

if negative:
    ax.annotate(f"Z = {Z_ohms} Ω", (R_ohms / 2, X_ohms / 2), textcoords="offset points", xytext=(0, 0), ha='center', fontsize=12, rotation=-phi_deg)
    ax.annotate(f"φ = -{phi_deg}°", (R_ohms / 5, X_ohms / 15), textcoords="offset points", xytext=(R_ohms / 15, -X_ohms / 10), ha='center', fontsize=12)
else:
    ax.annotate(f"Z = {Z_ohms} Ω", (R_ohms / 2, X_ohms / 2), textcoords="offset points", xytext=(0, 0), ha='center', fontsize=12, rotation=phi_deg)
    ax.annotate(f"φ = {phi_deg}°", (R_ohms / 5, 0), textcoords="offset points", xytext=(R_ohms / 15, X_ohms / 15), ha='center', fontsize=12)

# Ukryj przeciwne osie X i Y
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Ogranicz osie
if negative:
    ax.set_ylim(X_ohms + 10, -5)

# Dodaj etykiety osi
ax.set_title(title, fontsize=14, pad=20)

# Zapisz rysunek do pliku PNG
file_name = title.replace(" ", "_").lower() + ".png"
plt.savefig(file_name, dpi=200, bbox_inches='tight')

# Wyświetl rysunek
plt.show()
