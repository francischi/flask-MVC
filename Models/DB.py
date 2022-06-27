import pymysql
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
db_setting = {
    "host" : config['MYSQL']['host'],
    "port" : int(config['MYSQL']['port']),
    "user" : config['MYSQL']['user'],
    "password" : config['MYSQL']['password'],
    "db" : config['MYSQL']['db'],
    "charset" : config['MYSQL']['charset']
}

class connector:
    def __init__(self):
        self.pymysql = pymysql

    def connect(self):
        return self.pymysql.connect(**db_setting,cursorclass=pymysql.cursors.DictCursor ,autocommit=True)

    def executeCommand(self,command):
        connect = self.connect()
        with connect.cursor() as cursor:
            cursor.execute(command)
            result = cursor.fetchall()
        connect.close()
        return result

# 將與DB連接部分實作一個class，解決耦合度太高的問題，也讓程式碼的部分更接近依賴注入的理念
# ，後續若要抽換與sql連結的package，也很方便，提高可維護性與降低了程式碼的耦合度