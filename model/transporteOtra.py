from sympy import *
import numpy as np

from model.db import DB


class TransporteOtra:
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
            self.matriz[i, 0] = expr_x.evalf(subs={x: self.valor_x(i)})
        # cálculo de la segunda condición inicial sin 4,0
        for j in range(1, self.n+1):
             self.matriz[self.m, j] = expr_t.evalf(subs={t: self.valor_t(j)})
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

