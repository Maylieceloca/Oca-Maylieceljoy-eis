from connector import connector

class Users:

    def check_user(username, pasword):
        query = "SELECT * FROM users WHERE username=%s AND password=%s"

        Connector.cursor.execute(query, (username, password))
        result = Connector.cursor.fetchrone()

        if len(result) > 1:
            return False

            return True