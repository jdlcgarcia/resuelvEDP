from model.db import DB

db = DB('demo')
db.create('ecuacion', '''id INTEGER PRIMARY KEY,
                            coeficiente INTEGER NOT NULL,
                            termino_independiente INTEGER NOT NULL,
                            resultado REAL NULL''')