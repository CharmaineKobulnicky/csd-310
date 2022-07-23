import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="#dontBreakMe1",
    database="pysports"
)

mycursor = mydb.cursor()

mycursor.execute("player (player_id '1', first_name 'John', last_name 'Smith'), (player_id '2', first_name 'Tim', last_name 'Walker')")

for player in mycursor:
    print(player)
    