import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="J72e#05t"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE vehicles")