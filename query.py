from Conection import *
from flask import render_template
from main import *
def insert_students(datos):
    ID_student=datos[1]
    Name=datos[0]
    password=datos[8]
    maximun_assignments=1
    busy_mentor=0
    email=str(ID_student)+'@globaluniversity.edu.mx'
    sql = "INSERT INTO students (id_students, email, password, name, maximum_assignments, busy_mentor) VALUES (%s, %s, %s, %s, %s, %s)"
    val = [(ID_student, email, password, Name, maximun_assignments, busy_mentor)]
    mycursor.executemany(sql, val)
    mydb.commit()

def insert_crude(datos):
    #generados default (se deben solicitar)
    cuatrimestre=1
    parcial=3

    ID_student = datos[1]
    algebra = datos[2]
    programacion = datos[3]
    realidad_social = datos[4]
    comunicacion = datos[5]
    fisica = datos[6]
    soluciones_ingenieria = datos[7]
    querer_ayudar = datos[9]
    hablar_publico = datos[10]
    bueno_explicando = datos[11]
    id_algebra = 1
    id_progra = 2
    id_realidad_social = 3
    id_comunicacion = 4
    id_fisica = 5
    id_soluciones_ingenieria = 6
    id_querer_ayudar = 7
    id_hablar_publico = 8
    id_bueno_explicando = 9

    #insert algebra
    sql = "INSERT INTO crude (id_students, id_class, skills_class, cuatrimestre, parcial) VALUES (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_algebra, algebra, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert fisica
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_fisica, fisica, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert programacion
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_progra, programacion, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert comunicacion
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_comunicacion, comunicacion, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert realidad social
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_realidad_social, realidad_social, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert soluciones
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_soluciones_ingenieria, soluciones_ingenieria, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert ayudar
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_querer_ayudar, querer_ayudar, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert hablar
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_hablar_publico, hablar_publico, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    # insert explicar
    sql = "insert into crude (id_students, id_class, skills_class, cuatrimestre, parcial) values (%s, %s, %s, %s, %s)"
    val = [(ID_student, id_bueno_explicando, bueno_explicando, cuatrimestre, parcial)]
    mycursor.executemany(sql, val)

    mydb.commit()


def insert_skills(ID_student,skills):
    id_algebra = 1
    id_progra = 2
    id_realidad_social = 3
    id_comunicacion = 4
    id_fisica = 5
    id_soluciones_ingenieria = 6

    # insert algebra
    sql = "insert into processed_data (id_students, id_class, qualification) values (%s, %s, %s)"
    val = [(ID_student, id_algebra, skills[0] )]
    mycursor.executemany(sql, val)

    # insert Programacion
    sql = "insert into processed_data (id_students, id_class, qualification) values (%s, %s, %s)"
    val = [(ID_student, id_progra, skills[1] )]
    mycursor.executemany(sql, val)

    # insert Análisis
    sql = "insert into processed_data (id_students, id_class, qualification) values (%s, %s, %s)"
    val = [(ID_student, id_realidad_social, skills[2] )]
    mycursor.executemany(sql, val)

    # insert Análisis
    sql = "insert into processed_data (id_students, id_class, qualification) values (%s, %s, %s)"
    val = [(ID_student, id_comunicacion, skills[3] )] 
    mycursor.executemany(sql, val)

    # insert soluciones
    sql = "insert into processed_data (id_students, id_class, qualification) values (%s, %s, %s)"
    val = [(ID_student, id_soluciones_ingenieria, skills[4] )] 
    mycursor.executemany(sql, val)

    # insert soluciones
    sql = "insert into processed_data (id_students, id_class, qualification) values (%s, %s, %s)"
    val = [(ID_student, id_fisica, skills[5] )] 
    mycursor.executemany(sql, val)

    mydb.commit()
