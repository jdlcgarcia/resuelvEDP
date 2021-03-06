import sqlite3


class DB(object):
    def __init__(self, nombre_db):
        self.sqliteConnection = sqlite3.connect(nombre_db + '.db')

    def execute(self, consulta, tipo_consulta):
        cursor = self.sqliteConnection.cursor()
        cursor.execute(consulta)

        rows = []
        if cursor.rowcount != 0:
            rows = cursor.fetchall()
        if tipo_consulta == 'insert':
            return cursor.lastrowid
        cursor.close()
        return rows

    def create(self, nombre_tabla, fields):
        query = '''CREATE TABLE ''' + nombre_tabla + '''(''' + fields + ''');'''
        self.execute(query, 'create')

    def select(self, nombre_tabla, campos):
        query = '''SELECT ''' + campos + ''' FROM ''' + nombre_tabla + ''';'''
        self.execute(query, 'select')

    def insert(self, nombre_tabla, ecuacion):
        lista_columnas = ', '.join(map(str, ecuacion.keys()))
        lista_valores = ', '.join(map(str, ecuacion.values()))
        query = '''INSERT INTO ''' + nombre_tabla
        query += ''' (''' + lista_columnas + ''')'''
        query += ''' VALUES (''' + lista_valores + ''');'''
        nuevo_id = self.execute(query, 'insert')
        self.sqliteConnection.commit()
        return nuevo_id

    def select_por_id(self, nombre_tabla, nombre_campo, valor_campo):
        query = '''SELECT * FROM ''' + nombre_tabla + ''' WHERE ''' + nombre_campo + ''' = ''' + valor_campo + ''';'''
        return self.execute(query, 'select')

    def update_por_id(self, nombre_tabla, campos, nombre_id, valor_id):
        query = ''' UPDATE ''' + nombre_tabla
        query += ''' SET '''
        lista_update = []
        for k, v in campos.items():
            lista_update.append(k + ''' = ''' + "'" + v + "'")
        query += ','.join(lista_update)
        query += ''' WHERE ''' + nombre_id + ''' = ''' + str(valor_id) + ''';'''

        self.execute(query, 'update')
        self.sqliteConnection.commit()
