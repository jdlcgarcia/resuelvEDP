from model.transporteOtra import TransporteOtra

ecuacion = TransporteOtra()
ecuacion.cargar(1)
print("La ecuación a resolver es "+ecuacion.imprimir())
ecuacion.evaluar()
print("Su mallado es:\n")
print(ecuacion.imprimir_matriz())
print("Los puntos solución son:\n")
print(ecuacion.imprimirPuntosSolucion())