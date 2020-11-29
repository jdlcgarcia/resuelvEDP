from model.db import DB

db = DB('demo')
db.create('ecuacion', '''id INTEGER PRIMARY KEY,
                            coeficiente INTEGER NOT NULL,
                            termino_independiente INTEGER NOT NULL,
                            resultado REAL NULL''')
db.create('ecuacion_segundo_grado', '''id INTEGER PRIMARY KEY,
                            coeficiente_A INTEGER NOT NULL,
                            coeficiente_B INTEGER NOT NULL,
                            coeficiente_C INTEGER NOT NULL,
                            resultado_1 REAL NULL,
                            resultado_2 REAL NULL''')