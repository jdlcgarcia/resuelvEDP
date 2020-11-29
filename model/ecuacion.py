class Ecuacion(object):
    def __init__(self):
        self.coeficiente = 0
        self.termino_independiente = 0

        while True:

            try:
                self.coeficiente = int(input("Por favor, introduce el coeficiente: "))
                break
            except ValueError:
                print("Error! El coeficiente introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:

            try:
                self.termino_independiente = int(input("Por favor, introduce el término independiente: "))
                break
            except ValueError:
                print("Error! El término introducido no es un número. Por favor, inténtelo de nuevo.")

    def imprimir(self):
        ecuacion = str(self.coeficiente) + "x "
        if self.termino_independiente > 0:
            ecuacion += "+"
        ecuacion += str(self.termino_independiente)
        ecuacion += " = 0"
        return ecuacion
