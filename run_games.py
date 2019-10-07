from connect_db import *
from games_class import *

server = 'localhost,1433'
database = 'my_game'
username = 'SA'
password = 'Passw0rd2018'

conn_gamesdb = GamesListings(server, database, username, password)

# # finding info postcode1
# #postcode_info = conn_gamesdb.find_postcode_info('E2 8LU')
# #postcode1 = postcode_info['result']['postcode']
# # finding long and lat for postcode1
# long1 = float(postcode_info['result']['longitude'])
# lat1 = float(postcode_info['result']['latitude'])
#
# # finding info postcode2
# #postcode_info = conn_gamesdb.find_postcode_info('EC2Y 5AS')
# postcode2 = postcode_info['result']['postcode']
# # finding long and lat for postcode2
# long2 = float(postcode_info['result']['longitude'])
# lat2 = float(postcode_info['result']['latitude'])
#
#
# #update location for postcode1
# conn_gamesdb.update_game_listing('game_listings', 'location', "'E2 8LU'", 2)
# conn_gamesdb.update_game_listing('game_listings', 'longitude', long1, 2)
# conn_gamesdb.update_game_listing('game_listings', 'latitude', lat1, 2)
#
# #update location for postcode2
# conn_gamesdb.update_game_listing('game_listings', 'location', "'EC2Y 5AS'", 3)
# conn_gamesdb.update_game_listing('game_listings', 'longitude', long2, 3)
# conn_gamesdb.update_game_listing('game_listings', 'latitude', lat2, 3)

# add a listing
#conn_gamesdb.add_a_listing(3, "'NBA 2K19'", 13.49, "'EC2Y 5AS'", long2, lat2)

# list all listings
#print(conn_gamesdb.list_all_games("game_listings"))

# read one listing
#print(conn_gamesdb.read_one_game_listing("game_listings", 2))

# conn_gamesdb.lat_info(postcode_info)

greeting = print("Hello, you have entered Game Tree. What would you like to do?")
print('(1) View all listings')
print('(2) View one listing')
print('(3) Add a game listing')
user_input = int(input("Enter your choice"))
while True:
    if user_input == 1:
        print(conn_gamesdb.list_all_games("game_listings"))
        user_input = int(input("Enter a choice again:"))
    elif user_input == 2:
        user_input = int(input("Enter a game ID:"))
        print(conn_gamesdb.read_one_game_listing(user_input))
        user_input = int(input("Enter a choice again:"))
    elif user_input == 3:
        print("You've chosen to add a game to our listing.")
        game_id = int(input("Assign your game an ID:"))
        game_name = input('Enter the name of the game:').capitalize().strip()
        game_price = (float(input('How much would you like to sell it for?')))
        game_location = input('Enter a location (postcode):')
        game_long_info = conn_gamesdb.find_long_info(game_location)
        game_lat_info = conn_gamesdb.find_lat_info(game_location)
        print(f'{game_name} has now been added to the listing!')
        conn_gamesdb.add_a_listing(game_id, game_name, game_price, game_location, game_long_info, game_lat_info)

        break
    else:
        print("I am not sure what you mean...")
        break
