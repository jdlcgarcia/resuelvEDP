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
db.create('edp_transporte', '''id INTEGER PRIMARY KEY,
                            a INTEGER NOT NULL,
                            b INTEGER NOT NULL,
                            c INTEGER NOT NULL,
                            d INTEGER NOT NULL,
                            m INTEGER NOT NULL,
                            n INTEGER NOT NULL,
                            p REAL NOT NULL,
                            progresion_tiempo INTEGER NOT NULL,
                            progresion_espacio INTEGER NOT NULL,
                            condicion_inicial_x TEXT NOT NULL,
                            condicion_inicial_t TEXT NOT NULL,
                            puntos_solucion TEXT NULL''')