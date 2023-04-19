import json
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kanh1133557799",
    database="car_mnt"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT status, COUNT(status) AS size_status FROM graph GROUP BY status")

myresult = mycursor.fetchall()

data = []

for x in myresult:
    data.append(x)

print(json.dumps(data))
