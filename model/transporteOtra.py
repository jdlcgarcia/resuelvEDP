from sympy import *
import numpy as np

class TransporteOtra:
    def __init__(self):
        self.a = 2
        self.b = 4
        self.c = 0
        self.d = 2

        self.m = 10
        self.n = 20
        self.h = (self.b - self.a)/self.m
        self.k = (self.d - self.c)/self.n
        self.p = 1/3

        self.r = -(self.p * self.k) / self.h

        self.progresion = {
            'tiempo': 1,
            'espacio': 1
        }

        self.matriz = np.empty((self.m+1, self.n+1))
        self.inicializarMatriz()
        self.condicion_inicial_x = "cos(pi*x)"
        self.condicion_inicial_t = "1"

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

    def inicializarMatriz(self):
        for i in range(self.m+1):
            for j in range(self.n+1):
                self.matriz[i, j] = None
        self.matriz[0, 0] = 0

    def imprimirMatriz(self):
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



