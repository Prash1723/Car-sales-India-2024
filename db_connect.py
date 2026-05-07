import mysql.connector
from mysql.connector import Error

class db_query:
    def __init__(self, query):
        self.query = query

    def run(self, query, params=None):
        # Establish mysql connection
        cnx = mysql.connector.connect(host="localhost", user="rider", password="Delhi2mumbai@", database="car_sales")

        # Create cursor
        mycursor = cnx.cursor()

        # Execute a query
        mycursor.execute(query)

        # Fetch results
        result = mycursor.fetchall()

        # Close the connection
        cnx.close()

        return result
