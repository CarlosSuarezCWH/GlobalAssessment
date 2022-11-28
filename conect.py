import mysql.connector

mydb = mysql.connector.connect(
  host="cwh1.kiubix.biz",
  user="fpryvvyl_cwg",
  password="FELDqXHfgTxv",
  database="fpryvvyl_global"

)
mycursor = mydb.cursor()
mycursor.execute("SHOW tables;")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

