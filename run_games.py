from connect_db import *
from games_class import *

server = 'localhost,1433'
database = 'my_game'
username = 'SA'
password = 'Passw0rd2018'

conn_gamesdb = GamesListings(server, database, username, password)


greeting = print("Hello, you have entered Game Tree. What would you like to do?")
print('(1) View all listings')
print('(2) View one listing')
print('(3) Add a game listing')
print('(4) Update a listing')
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
    elif user_input == 4:
        print("You have chosen to update a listing.")
        print(conn_gamesdb.list_all_games("game_listings"))
        user_input = input("Which listing would you like to update?")
        while True:
            if user_input == "Mario kart":
                conn_gamesdb.update_game_listing("game_id", "4", "21")
                print("Your listing has now been updated!")
                break
            elif user_input == "Spider-Man":
                conn_gamesdb.update_game_listing("location", "'UB2 5QH'", "2")
                print("Your listing has now been updated!")
            else:
                print("Try again")
    else:
        print("I am not sure what you mean...")
        break
