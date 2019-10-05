from connect_db import *
import requests
import json

# child-class inheriting from connect_db (Parent class)

class GamesListings(ConnectionMicrosoftServer):

    # Create a games listing
    def add_a_listing(self, game_id, name, price, location, longitude, latitude):
        query_rows = self.filter_query(f"INSERT INTO game_listings VALUES ({game_id}, {name},{price}, {location}, {longitude}, {latitude}")
        self.conn_gamesdb.commit()

    # Read a listing
    def read_one_game_listing(self, table, game_id):
        query = self.filter_query(f"SELECT * FROM {table} WHERE recipe_id = {game_id}")
        while True:
            record = query.fetchone()
            if record is None:
                break
            return record

    # Listing all games
    def list_all_games(self, table):
        query = self.filter_query(f"SELECT * FROM {table}")
        while True:
            record = query.fetchall()
            if record is None:
                break
            return record

    # Postcode info
    def find_postcode_info(self, postcode):
        postcode_query = requests.get('http://api.postcodes.io/postcodes/' + postcode)
        result = postcode_query.json()
        return result

# As a user I want to insert a location to my listing (e.g. 125 London Wall) and I want it on my Db
# As a user I want to be able to see a longitude and latitude to my listing and be on my Db