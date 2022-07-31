import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="pysports_cha",
    passwd="$lady#",
    database="pysports"
)

mycursor = mydb.cursor()

mycursor.execute("player (player_id '1', first_name 'John', last_name 'Smith', team_id '10'), (player_id '2', first_name 'Tim', last_name 'Walker', team_id '10'), (player_id '3', first_name 'Cris', last_name 'Dur', team_id '10'), (player_id '4', first_name 'Jane', last_name 'Huss', team_id '11'), (player_id '5', first_name 'Lis', last_name 'Mye', team_id '11'), (player_id '6', first_name 'Ric', last_name 'Dre', team_id '11')")

for player in mycursor:
    print(player)
    