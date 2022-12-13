def lista_limpia(datos):
    datos[0]="x"
    datos[1]="x"
    datos[-1]="x"
    lista=[]
    for i in datos:
        try:
            i=float(i)
            lista.append(i)
        except:
            i="0"
    return lista

def Skills(datos):
    lista=lista_limpia(datos)
    skills=[]
    for i in range(6):
        calificacion=lista[i]
        skill=(calificacion*lista[-1]*0.8)+((lista[6]+lista[7]+lista[8]+(lista[9]+1))*5)
        skills.append(skill)
    return skills





