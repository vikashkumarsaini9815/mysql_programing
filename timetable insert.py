
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)

mycursor = mydb.cursor()

sql = "INSERT INTO timetable(s_no,stu_id,dates, times_morning,time_evening) VALUES (%s, %s,%s,%s,%s)"
val = [(5,4144,'2021-04-26','09:30:30','16:30:30'),
       (6,49549,'2021-03-25','07:00:00','13:00:00')]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


