from model.db import DB


class Ecuacion(object):
    def __init__(self):
        self.id = 0
        self.coeficiente = 0
        self.termino_independiente = 0
        self.solucion = 0

    def get_id(self):
        return self.id

    def pedir_datos(self):
        while True:

            try:
                self.coeficiente = int(input("Por favor, introduce el coeficiente de x: "))
                break
            except ValueError:
                print("Error! El coeficiente introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:

            try:
                self.termino_independiente = int(input("Por favor, introduce el término independiente: "))
                break
            except ValueError:
                print("Error! El término introducido no es un número. Por favor, inténtelo de nuevo.")

        db = DB('demo')
        self.id = db.insert('ecuacion', {
            'coeficiente': self.coeficiente,
            'termino_independiente': self.termino_independiente
        })

    def cargar(self, identificador):
        db = DB('demo')
        ecuacion = db.select_por_id('ecuacion', 'id', str(identificador))
        self.coeficiente = ecuacion[0][1]
        self.termino_independiente = ecuacion[0][2]

    def imprimir(self):
        ecuacion = str(self.coeficiente) + "x "
        if self.termino_independiente > 0:
            ecuacion += "+"
        ecuacion += str(self.termino_independiente)
        ecuacion += " = 0"
        return ecuacion

    def resolver(self):
        self.solucion = -self.termino_independiente / self.coeficiente

    def obtener_solucion(self):
        return self.solucion
