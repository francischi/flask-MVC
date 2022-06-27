from . import DB
class User:
    def __init__(self):
        self.table = "user"
        self.connector = DB.connector()
    def getAll(self):
        try:
            command = "SELECT * FROM "+self.table
            result  =  self.connector.executeCommand(command)
            return result
        except Exception as msg:
            raise ValueError(msg)

     
