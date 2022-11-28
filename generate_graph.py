from main import *
import numpy as np
from obtainForm import calificacion_skills


def graph():
    import matplotlib.pyplot as plt
    Clases = ['Algebra', 'Programacion', 'Analisis de la realidad', 'Comunicacion', 'Fisica',
              ' Soluciones de ingenieria']
    Skills = calificacion_skills(skills)
    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(Skills))
    plt.figure(figsize=(8, 8))
    plt.subplot(polar=True)
    plt.plot(label_loc, Skills)
    lines, labels = plt.thetagrids(np.degrees(label_loc), labels=Clases)
    plt.legend()
    plt.show()
