from main import *
import numpy as np
import matplotlib.pyplot as plt


Clases = ['Algebra', 'Programacion', 'Analisis de la realidad', 'Comunicacion', 'Fisica', ' Soluciones de ingenieria']

Skills = Calculate(algebra, programacion, analisis, comunicacion, fisica, ingenieria)
label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(restaurant_1))

plt.figure(figsize=(8, 8))
plt.subplot(polar=True)
plt.plot(label_loc, Skills)
lines, labels = plt.thetagrids(np.degrees(label_loc), labels=Clases)
plt.legend()
plt.show()