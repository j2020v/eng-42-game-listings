import pyodbc

class ConnectionMicrosoftServer():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_gamesdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_gamesdb.cursor()

    def filter_query(self, query):
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.filter_query(query).execute(query)

    def sql_query_fetchone(self, query):
        return self.filter_query(query).fetchone()

