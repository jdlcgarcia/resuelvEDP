import sqlite3


class DB(object):
    def __init__(self, nombre_db):
        self.sqliteConnection = sqlite3.connect(nombre_db + '.db')

    def execute(self, consulta):
        cursor = self.sqliteConnection.cursor()
        cursor.execute(consulta)
        cursor.close()

    def create(self, nombre_tabla, fields):
        query = '''CREATE TABLE ''' + nombre_tabla + '''(''' + fields + ''');'''
        print(query)
        self.execute(query)

    def select(self, nombre_tabla, campos):
        query = '''SELECT ''' + campos + ''' FROM ''' + nombre_tabla + ''';'''
        self.execute(query)
