import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="J72e#05t",
    database = "vehicles"
)

mycursor = mydb.cursor()

sql = "INSERT INTO final (license_plate, entry_time, status, exit_time) VALUES (%s, %s, %s, %s)"
val = ('AP26L348', '12:30', 'in', 'ss')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")