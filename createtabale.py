import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE students(stu_id INT (5),Name VARCHAR (200),Roll_no INT (8),Address varchar(50),mobile_no INT (10))")


