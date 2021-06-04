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
print(myresult)

for row in myresult:
  morningtime=row[3]
  eveningtime=row[4]
  spendtime=eveningtime - morningtime
  sql="UPDATE timetable SET discription='{}' WHERE s_no={}".format(str(spendtime),str(row[0]))
  #print(row)
  #print (sql)
  mycursor.execute(sql)
  #print(morningtime)
  #print(eveningtime)
  #print(spendtime)
  
  
