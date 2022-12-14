def lista_limpia(datos):
    datos2=datos
    datos2[0]="x"
    datos2[1]="x"
    datos2[-1]="x"
    lista=[]
    for i in datos2:
        try:
            i=float(i)
            lista.append(i)
        except:
            i="0"
    return lista

def Skills(datos):
    lista=lista_limpia(datos)
    skills=[]
    if lista[9] == 0:
        lista[9]=1
    else:
        lista[9]=0
    for i in range(6):
        calificacion=lista[i]
        skill=(calificacion*lista[-1]*0.8)+((lista[6]+lista[7]+lista[8]+lista[9])*5)
        skills.append(skill)
    return skills







