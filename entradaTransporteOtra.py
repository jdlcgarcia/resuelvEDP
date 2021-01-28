from model.transporteOtra import TransporteOtra

ecuacion = TransporteOtra()
print("La ecuación a resolver es "+ecuacion.imprimir())
ecuacion.evaluar()
print("Su matriz es:\n")
print(ecuacion.imprimirMatriz())
print("Los puntos solución son:\n")
print(ecuacion.imprimirPuntosSolucion())