import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("DESC students")

for x in mycursor:
  print(x)
