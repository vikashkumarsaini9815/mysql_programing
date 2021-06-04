import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="school"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (stu_id,Roll_no,Name,Mobile_no,Address) VALUES (%s, %s, %s, %s, %s )"
val = [(3,1115, "vicky",27398,"dehli"),
       (5,4516, "siv",65393,"kolkata"),
       (6,84957,"lalchand",85648,"khejroli"),
       (7,67483,"nena",54748,"dheradun"),
       (8,9098,"vijay",46437,"benglore"),
       (9,54398,"suman",64743,"mumbai"),
       (10,7585,"pooja",75347,"churu")
      ]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


