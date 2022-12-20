import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="J72e#05t",
    database = "vehicles"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE final (license_plate VARCHAR(255), entry_time VARCHAR(255), status VARCHAR(255), exit_time VARCHAR(255))")

mydb.commit()
