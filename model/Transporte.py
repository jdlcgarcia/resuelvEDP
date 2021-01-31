from mpl_toolkits.mplot3d import Axes3D
from sympy import *
import numpy as np
from model.DB import DB
import matplotlib.pyplot as plt
from matplotlib import cm


class Transporte:
    def __init__(self):
        self.id = None
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        self.m = 0
        self.n = 0
        self.p = 0

        self.h = None
        self.k = None
        self.r = None
        self.matriz = None

        self.progresion = {
            'tiempo': 0,
            'espacio': 0
        }
        self.condicion_inicial_x = ""
        self.condicion_inicial_t = ""

    def get_id(self):
        return self.id

    def inicializar_estructura(self):
        self.h = (self.b - self.a) / self.m
        self.k = (self.d - self.c) / self.n
        self.r = -(self.p * self.k) / self.h
        self.matriz = np.empty((self.m + 1, self.n + 1))
        self.inicializar_matriz()

    def valor_x(self, i):
        return self.a + i * self.h

    def valor_t(self, j):
        return self.c + j * self.k

    def imprimir(self):
        ecuacion = "u_t "
        if self.p > 0:
            ecuacion += "+ "
        ecuacion += str(self.p) + "u_x "
        ecuacion += " = 0\n"
        ecuacion += "u(x,0) = " + self.condicion_inicial_x + "\n"
        ecuacion += "u(0,t) = " + self.condicion_inicial_t + "\n"

        return ecuacion

    def inicializar_matriz(self):
        for i in range(self.m + 1):
            for j in range(self.n + 1):
                self.matriz[i, j] = None
        self.matriz[0, 0] = 0

    def imprimir_matriz(self):
        for j in range(self.n, -1, -1):
            print(j, end=') ')
            for i in range(self.m + 1):
                print(self.matriz[i, j], end=' ')
            print('')

    @staticmethod
    def print_coord(i, j):
        print(i, end=',')
        print(j)

    def extraer_puntos_solucion(self):
        solucion = []
        for j in range(self.n + 1):
            for i in range(self.m + 1):
                coordenada = self.punto_solucion_por_coordenada(i, j)
                solucion.append(coordenada)
        return solucion

    def punto_solucion_por_coordenada(self, i, j):
        punto_solucion = {}
        punto_solucion.update({"x": self.valor_x(i)})
        punto_solucion.update({"t": self.valor_t(j)})
        punto_solucion.update({"solucion": self.matriz[i, j]})
        return punto_solucion

    def cargar(self, identificador):
        db = DB('demo')
        ecuacion = db.select_por_id('edp_transporte', 'id', str(identificador))
        if not ecuacion:
            print("Ecuación no encontrada")
            return false

        self.id = identificador
        self.a = ecuacion[0][1]
        self.b = ecuacion[0][2]
        self.c = ecuacion[0][3]
        self.d = ecuacion[0][4]
        self.m = ecuacion[0][5]
        self.n = ecuacion[0][6]
        self.p = ecuacion[0][7]
        self.progresion = {
            'tiempo': ecuacion[0][8],
            'espacio': ecuacion[0][9]
        }
        self.condicion_inicial_x = ecuacion[0][10]
        self.condicion_inicial_t = ecuacion[0][11]
        self.inicializar_estructura()
        return true

    def pedir_datos(self):
        while True:
            try:
                self.a = int(input("Por favor, introduzca el primer componente del intervalo de x: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.b = int(input("Por favor, introduzca el segundo componente del intervalo de x: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.c = int(input("Por favor, introduzca el primer componente del intervalo de t: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.d = int(input("Por favor, introduzca el segundo componente del intervalo de t: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.m = int(input("Por favor, introduzca el número de nodos que se desean en el eje x: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.n = int(input("Por favor, introduzca el número de nodos que se desean en el eje y: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.p = float(input("Por favor, introduzca el coeficiente de Ux: "))
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.progresion['tiempo'] = int(
                    input("Por favor, introduzca el esquema en el tiempo: (1) progresivo, (0) regresivo: ")
                )
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.progresion['espacio'] = int(
                    input("Por favor, introduzca el esquema en el espacio: (1) progresivo, (0) regresivo: ")
                )
                break
            except ValueError:
                print("Error! El dato introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.condicion_inicial_x = input("Por favor, introduzca la condición inicial en x: ")
                break
            except ValueError:
                print("Error! la condicion inicial en x no es válida. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.condicion_inicial_t = input("Por favor, introduzca la condicion inicial en t: ")
                break
            except ValueError:
                print("Error! la condicion inicial en t no es válida. Por favor, inténtelo de nuevo.")
        db = DB('demo')
        self.id = db.insert('edp_transporte', {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            'm': self.m,
            'n': self.n,
            'p': self.p,
            'progresion_tiempo': self.progresion['tiempo'],
            'progresion_espacio': self.progresion['espacio'],
            'condicion_inicial_x': '"' + self.condicion_inicial_x + '"',
            'condicion_inicial_t': '"' + self.condicion_inicial_t + '"',
        })

    def guardar_solucion(self):
        db = DB('demo')
        campos = {'puntos_solucion': self.aplanar_solucion()}
        db.update_por_id('edp_transporte', campos, 'id', self.id)
        self.pintar_grafico()

    def aplanar_solucion(self):
        solucion = self.extraer_puntos_solucion()
        aplanada = []
        for i in solucion:
            aplanada.append('{' + str(i['x']) + ', ' + str(i['t']) + ', ' + str(i['solucion']) + '}')
        return ','.join(aplanada)

    def pintar_grafico(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        solucion = self.extraer_puntos_solucion()
        x = []
        y = []
        z = []
        for i in solucion:
            x.append(i['x'])
            y.append(i['t'])
            z.append(i['solucion'])

        surf = ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.1)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
        plt.draw()
        fig.savefig('grafico'+str(self.id)+'.png', dpi=100)
