import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)
def inserts (no,stu_id,dates,times,time):
        
        mycursor = mydb.cursor()
        
        sql = "INSERT INTO timetable(s_no,stu_id,dates, times_morning,time_evening) VALUES (%s, %s,%s,%s,%s)"
        val = (no,stu_id,dates,times,time)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
inserts (9,484,'2021-02-05','04:00:00','13:00:00')

