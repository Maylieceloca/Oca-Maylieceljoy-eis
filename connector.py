import mysql.connector

class connector:
     db = mysql.connector.connect(host ="localhost", user="root", password="", db="inventory_system")
     cursor = db.cursor