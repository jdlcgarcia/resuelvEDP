from sympy import *
import numpy as np

class Transporte:
    def __init__(self):
        self.puntos = {
            'x': 12,
            'y': 6
        }
        self.h = 1/self.puntos['x']
        self.k = 1/self.puntos['y']
        self.p = 4
        self.r = -self.p*self.k/self.h
        self.progresion = {
            'tiempo': 1,
            'espacio': 1
        }
        self.matriz = np.empty((self.puntos['x'], self.puntos['y']))
        self.inicializarMatriz()
        self.condicion_inicial_x = "sin(pi*x)"
        self.condicion_inicial_t = "0"

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
        for i in range(self.puntos['x']):
            for j in range(self.puntos['y']):
                self.matriz[i, j] = None

    def imprimirMatriz(self):
        for j in range(self.puntos['y']-1, 0, -1):
            for i in range(self.puntos['x']):
                print(self.matriz[i, j], end=' ')
            print('')

    def evaluar(self):
        x, t = symbols('x, t')
        expr_x = sympify(self.condicion_inicial_x)
        expr_t = sympify(self.condicion_inicial_t)
        # cálculo de la primera condición inicial
        for i in range(self.puntos['x']):
            respuesta = expr_x.evalf(subs={x: i})
            self.matriz[i, 0] = respuesta
        # cálculo de la segunda condición inicial sin 0,0
        for j in range(1, self.puntos['y']):
            respuesta = expr_t.evalf(subs={t: i})
            self.matriz[0, j] = respuesta
        # cálculo del caso general
        for j in range(1, self.puntos['y']):
            for i in range(1, self.puntos['x']):
                respuesta = self.matriz[i, j-1] + self.r*(self.matriz[i, j-1] - self.matriz[i-1, j-1])
                self.matriz[i, j] = respuesta


