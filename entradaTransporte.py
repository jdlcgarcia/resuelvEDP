from model.transporte import Transporte

ecuacion = Transporte()
print("La ecuación a resolver es "+ecuacion.imprimir())
ecuacion.evaluar()
print("Su matriz es:\n")
print(ecuacion.imprimirMatriz())