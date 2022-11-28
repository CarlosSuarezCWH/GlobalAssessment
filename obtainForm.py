from main import *
import matplotlib.pyplot as plt
def calificacion_skills(calificacion,hablar,explicar,socializar,puede_ayudar,quiere_ayudar):
    if hablar == 1: hablar = 0
    elif hablar == 0: hablar= 1
    s1=hablar*5+puede_ayudar*15+socializar*10
    if calificacion < 10 and calificacion >= 8 and explicar == 9:
        s2=calificacion*7
    elif calificacion <10 and calificacion >=8 and explicar ==10:
        s2=calificacion*7+10
    elif calificacion==10 and explicar >= 8:
        s2=calificacion*7
    elif calificacion==10 and explicar < 8:
        s2=((calificacion*.1*explicar)*7)+10
    else:
        s2=(calificacion*(.1*explicar)*7)
    if s2 > 70:
        s2=70
    if s2 >= 63 and s2 < 70 and s1 < 26:
        skill = (s1+s2+2)*quiere_ayudar
    elif s2 == 70 and s1 < 26:
            skill = (s1+s2+5)*quiere_ayudar
    else:
        skill=(s1+s2)*quiere_ayudar
    if skill > 10: skill = skill - 10
    return skill
def Calculate(algebra, programacion, analisis, comunicacion, fisica, ingenieria,hablar,explicar,socializar,puede_ayudar,quiere_ayudar):
    algebra=calificacion_skills(algebra,float(hablar),explicar,float(socializar),float(puede_ayudar),float(quiere_ayudar))
    programacion=calificacion_skills(programacion,float(hablar),explicar,float(socializar),float(puede_ayudar),float(quiere_ayudar))
    analisis=calificacion_skills(analisis,float(hablar),explicar,float(socializar),float(puede_ayudar),float(quiere_ayudar))
    comunicacion=calificacion_skills(comunicacion,float(hablar),explicar,float(socializar),float(puede_ayudar),float(quiere_ayudar))
    fisica=calificacion_skills(fisica,float(hablar),explicar,float(socializar),float(puede_ayudar),float(quiere_ayudar))
    ingenieria=calificacion_skills(ingenieria,float(hablar),explicar,float(socializar),float(puede_ayudar),float(quiere_ayudar))
    return algebra, programacion, analisis, comunicacion, fisica, ingenieria


