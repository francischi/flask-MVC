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