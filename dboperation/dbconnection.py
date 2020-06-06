import mysql.connector as mysqldb


class DatabaseConnection():
    @staticmethod
    def createconnection():
        dbcon = mysqldb.connect(host="localhost", user="root", passwd="root", database="clerk")
        return dbcon

