from sympy import *


class transporte_progresiva_regresiva:
    def __init__(self, edp):
        self.ecuacion = edp
        
    def evaluar(self):
        x, t = symbols('x, t')
        expr_x = sympify(self.ecuacion.condicion_inicial_x)
        expr_t = sympify(self.ecuacion.condicion_inicial_t)
        # cálculo de la primera condición inicial
        self.primera_horizontal(expr_x, t, x)
        # cálculo de la segunda condición inicial sin 4,0
        self.primera_vertical(expr_t, t, x)
        # cálculo del caso general
        for j in range(1, self.ecuacion.n+1):
            for i in range(self.ecuacion.m-1, -1, -1):
                self.ecuacion.matriz[i, j] = self.ecuacion.r * (self.ecuacion.matriz[i+1, j-1] - self.ecuacion.matriz[i, j-1])+self.ecuacion.matriz[i, j-1]

    def primera_vertical(self, expr_t, t, x):
        for j in range(1, self.ecuacion.n + 1):
            self.ecuacion.matriz[0, j] = expr_t.evalf(
                subs={x: self.ecuacion.valor_x(self.ecuacion.m), t: self.ecuacion.valor_t(j)})

    def primera_horizontal(self, expr_x, t, x):
        for i in range(self.ecuacion.m + 1):
            self.ecuacion.matriz[i, 0] = expr_x.evalf(subs={x: self.ecuacion.valor_x(i), t: self.ecuacion.valor_t(0)})


