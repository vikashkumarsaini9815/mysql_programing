import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM timetable")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
