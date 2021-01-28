from sympy import *
import numpy as np

from model.db import DB


class transporte:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        self.m = 0
        self.n = 0
        self.p = 0

        self.progresion = {
            'tiempo': 1,
            'espacio': 1
        }
        self.condicion_inicial_x = ""
        self.condicion_inicial_t = ""

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
        for i in range(self.m+1):
            for j in range(self.n+1):
                self.matriz[i, j] = None
        self.matriz[0, 0] = 0

    def imprimir_matriz(self):
        for j in range(self.n, -1, -1):
            print(j, end=') ')
            for i in range(self.m+1):
                print(self.matriz[i, j], end=' ')
            print('')

    def evaluar(self):
        x, t = symbols('x, t')
        expr_x = sympify(self.condicion_inicial_x)
        expr_t = sympify(self.condicion_inicial_t)
        # cálculo de la primera condición inicial
        for i in range(self.m+1):
            self.matriz[i, 0] = expr_x.evalf(subs={x: self.valor_x(i), t:self.valor_t(0)})
        # cálculo de la segunda condición inicial sin 4,0
        for j in range(1, self.n+1):
             self.matriz[self.m, j] = expr_t.evalf(subs={x: self.valor_x(self.m), t: self.valor_t(j)})
        # cálculo del caso general
        for j in range(1, self.n+1):
            for i in range(self.m-1, -1, -1):
                self.matriz[i, j] = self.r * (self.matriz[i+1, j-1] - self.matriz[i, j-1])+self.matriz[i, j-1]

    def print_coord(self, i, j):
        print(i, end=',')
        print(j)

    def imprimirPuntosSolucion(self):
        for j in range(self.n + 1):
            for i in range(self.m+1):
                self.print_solucion(i, j)
        return ""

    def print_solucion(self, i, j):
        print("{", end='')
        print(self.valor_x(i), end=', ')
        print(self.valor_t(j), end=', ')
        print(self.matriz[i, j], end='},')

    def cargar(self, identificador):
        db = DB('demo')
        ecuacion = db.select_por_id('edp_transporte', 'id', str(identificador))
        if not ecuacion:
            print("Ecuación no encontrada")
            return false

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
                self.a = int(input("Por favor, a: "))
                break
            except ValueError:
                print("Error! El a introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.b = int(input("Por favor, b: "))
                break
            except ValueError:
                print("Error! El b introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.c = int(input("Por favor, c: "))
                break
            except ValueError:
                print("Error! El c introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.d = int(input("Por favor, d: "))
                break
            except ValueError:
                print("Error! El d introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.m = int(input("Por favor, m: "))
                break
            except ValueError:
                print("Error! El m introducido no es un número. Por favor, inténtelo de nuevo.")

        while True:
            try:
                self.n = int(input("Por favor, n: "))
                break
            except ValueError:
                print("Error! El n introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.p = float(input("Por favor, p: "))
                break
            except ValueError:
                print("Error! El p introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.tiempo = int(input("Por favor, tiempo: "))
                break
            except ValueError:
                print("Error! El tiempo introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.espacio = int(input("Por favor, espacio: "))
                break
            except ValueError:
                print("Error! El espacio introducido no es un número. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.condicion_inicial_x = input("Por favor, condicion inicial x: ")
                break
            except ValueError:
                print("Error! la condicion inicial X no es válida. Por favor, inténtelo de nuevo.")
        while True:
            try:
                self.condicion_inicial_t = input("Por favor, condicion inicial t: ")
                break
            except ValueError:
                print("Error! la condicion inicial t no es válida. Por favor, inténtelo de nuevo.")
        db = DB('demo')
        db.insert('edp_transporte', {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            'm': self.m,
            'n': self.n,
            'p': self.p,
            'progresion_tiempo': self.tiempo,
            'progresion_espacio': self.espacio,
            'condicion_inicial_x': self.condicion_inicial_x,
            'condicion_inicial_t': self.condicion_inicial_t,
        })