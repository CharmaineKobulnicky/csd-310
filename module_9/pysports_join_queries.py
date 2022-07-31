import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_cha",
    "password": "$lady#",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    """ try/catch block for handling potential MySQL database errors """

    db = mysql.connector.connect(**config) # connect to the pysports database

    cursor = db.cursor()

    # inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

    # left outer join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player LEFT OUTER JOIN team ON player.team_id = team.team_id;")

    # right outer join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player RIGHT OUTER JOIN team ON player.team_id = team.team_id;")

    # where clause query
    cursor.execute("SELECT first_name, last_name FROM player WHERE player_id = 3;")

    # get the results from the cursor object
    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS --")

    # iterate over the player data set and display the results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n.format(player[0], player[1], player[2], player[3])")

    input("\n\n Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """
 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

finally:
    """ close the connection to MySQL """

    db.close()
    
