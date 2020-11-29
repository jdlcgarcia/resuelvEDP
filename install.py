from model.db import DB

db = DB('demo')
db.create('segundo_grado', '''id INTEGER PRIMARY KEY,
                            coeficiente_a INTEGER NOT NULL,
                            coeficiente_b INTEGER NOT NULL,
                            coeficiente_c INTEGER,
                            resultado_1 REAL,
                            resultado_2 REAL''')