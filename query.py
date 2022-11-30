from Conection import *
from main import *
def insert_crude(ID_student,password,Name):
    ID_student=data(ID_student)
    maximun_assignments=1
    busy_mentor=0
    email=str(ID_student)*'@globaluniversity.edu.mx'
    sql = "INSERT INTO crude (id_students, email, password, name, maximum_assignments, busy_mentor) VALUES (%s, %s)"
    val = [(ID_student, email, password, Name, maximun_assignments, busy_mentor)]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")