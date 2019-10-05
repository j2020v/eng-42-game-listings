from connect_db import *
from games_class import *

server = 'localhost,1433'
database = 'my_game'
username = 'SA'
password = 'Passw0rd2018'

conn_gamesdb = GamesListings(server, database, username, password)

# finding a postcode
postcode_info = conn_gamesdb.find_postcode_info('EC2Y 5AS')
postcode1 = (postcode_info['result']['postcode'])

# finding long and lat for postcode1
long1 = int(postcode_info['result']['longitude'])
lat1 = int(postcode_info['result']['latitude'])

# add a listing
#conn_gamesdb.add_a_listing(4, "'Mark of the Ninja'", 6.90 + postcode1, long1, lat1)

#postcode2info = conn_gamesdb.find_postcode_info('E2 8LU')
#postcode3info = conn_gamesdb.find_postcode_info('E9 6RY')

# finding long and lat for postcode2
#long2 = (postcode2['result']['longitude'])
#lat2 = (postcode2['result']['latitude'])

# finding long and lat for postcode3
#long3 = (postcode3['result']['longitude'])
#lat3 = (postcode3['result']['latitude'])


# list all listings
#print(conn_gamesdb.list_all_games("game_listings"))

# read one listing
#print(conn_gamesdb.read_one_game_listing("game_listings", 2))