from connect_db import *
import requests
import json

# child-class inheriting from connect_db (Parent class)

class GamesListings(ConnectionMicrosoftServer):

    # Create a games listing
    def add_a_listing(self, game_id, name, price, location, longitude='', latitude=''):
        query = (f"INSERT INTO game_listings VALUES ({game_id}, '{name}', {price}, '{location}', '{longitude}', '{latitude}')")
        self.filter_query(query)
        self.conn_gamesdb.commit()

    # Read a listing
    def read_one_game_listing(self, game_id):
        query = self.filter_query(f"SELECT * FROM game_listings WHERE game_id = {game_id}")
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
    def find_long_info(self, postcode):
        postcode_query = requests.get(f'http://api.postcodes.io/postcodes/'+ postcode)
        result_postcode_query = postcode_query.json()
        long = result_postcode_query['result']['longitude']
        self.conn_gamesdb.commit()
        return float(long)

    def find_lat_info(self, postcode):
        postcode_query = requests.get(f'http://api.postcodes.io/postcodes/' + postcode)
        result_postcode_query = postcode_query.json()
        lat = result_postcode_query['result']['latitude']
        self.conn_gamesdb.commit()
        return float(lat)

    # Update listing
    def update_game_listing(self, column, value, game_id):
        query = f"UPDATE game_listings SET {column} = {value} WHERE game_id = {game_id}"
        self.filter_query(query)
        self.conn_gamesdb.commit()

    # Delete listing
    def delete_game_listing(self, game_id):
        query = f"DELETE FROM game_listings WHERE game_id = {game_id}"
        self.filter_query(query)
        self.conn_gamesdb.commit()

