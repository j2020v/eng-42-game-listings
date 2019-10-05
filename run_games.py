from connect_db import *
from games_class import *

server = 'localhost,1433'
database = 'my_game'
username = 'SA'
password = 'Passw0rd2018'

conn_gamesdb = GamesListings(server, database, username, password)

# add a listing
conn_gamesdb.add_a_listing(3, "'Spider-Man'", 23.85, "'HA5 5NZ'", "'-0.379288'", "'51.587946'")

# list all listings
#print(conn_gamesdb.list_all_games("game_listings"))


