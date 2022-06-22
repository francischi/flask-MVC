from . import DB
class User:
    def __init__(self):
        self.table = "user"
        self.connector = DB.connector()
    def getAll(self):
        try:
            connect = self.connector.connect()
            with connect.cursor() as cursor:
                command = "SELECT * FROM "+self.table
                cursor.execute(command)
                result = cursor.fetchall()
            connect.close()
            return result
        except Exception as msg:
            raise ValueError(msg)

     
