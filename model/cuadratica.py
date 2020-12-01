from numpy import sqrt

from model.db import DB
from model.ecuacion import Ecuacion


class Cuadratica(Ecuacion):
    def __init__(self):
        Ecuacion.__init__(self)
        self.coeficiente_a = 0
        self.coeficiente_b = 0
        self.coeficiente_c = 0
        self.solucion_1 = 0
        self.solucion_2 = 0

    def pedir_datos(self):
        while True:

            try:
                self.coeficiente_a = int(input("Por favor, introduce el coeficiente de x^2: "))
                break
            except ValueError:
                print("Error! El coeficiente introducido no es un número. Por favor, inténtelo de nuevo.")

        Ecuacion.pedir_datos(self)
        self.coeficiente_b = self.coeficiente
        self.coeficiente_c = self.termino_independiente

        db = DB('demo')
        coeficientes = {
            'coeficiente_a': self.coeficiente_a,
            'coeficiente_b': self.coeficiente_b,
            'coeficiente_c': self.coeficiente_c,
        }
        db.insert('ecuacion_segundo_grado', coeficientes)

    def cargar(self, identificador):
        db = DB('demo')
        ecuacion = db.select_por_id('ecuacion_segundo_grado', 'id', str(identificador))
        self.coeficiente_a = ecuacion[0][1]
        self.coeficiente_b = ecuacion[0][2]
        self.coeficiente_c = ecuacion[0][3]

    def imprimir(self):
        ecuacion = str(self.coeficiente_a) + "x^2 "
        if self.coeficiente_b > 0:
            ecuacion += "+"
        ecuacion += str(self.coeficiente_b) + "x "
        if self.coeficiente_c > 0:
            ecuacion += "+"
        ecuacion += str(self.coeficiente_c)
        ecuacion += " = 0"
        return ecuacion

    def resolver(self):
        discriminante = self.coeficiente_b ** 2 - 4 * self.coeficiente_a * self.coeficiente_c
        if discriminante > 0:
            self.solucion_1 = (-self.coeficiente_b + sqrt(discriminante)) / (2 * self.coeficiente_a)
            self.solucion_2 = (-self.coeficiente_b - sqrt(discriminante)) / (2 * self.coeficiente_a)
        else:
            self.solucion_1 = complex(-self.coeficiente_b / (2 * self.coeficiente_a),
                                      sqrt(-discriminante) / (2 * self.coeficiente_a))
            self.solucion_2 = complex(-self.coeficiente_b / (2 * self.coeficiente_a),
                                      -sqrt(-discriminante) / (2 * self.coeficiente_a))

    def obtener_solucion(self):
        return [self.solucion_1, self.solucion_2]
