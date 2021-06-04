import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)
def selects ():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM timetable")
        myresult = mycursor.fetchall()
        print(myresult)
#selects ()

# second method
def selects (Tb):
        mycursor = mydb.cursor()
        mycursor.execute(Tb)
        myresult = mycursor.fetchall()
        print(myresult)
selects ("SELECT * FROM timetable")
