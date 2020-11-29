from model.cuadratica import Cuadratica

ecuacion = Cuadratica()
ecuacion.cargar(1)
print("La ecuación a resolver es "+ecuacion.imprimir())
ecuacion.resolver()
print("Las soluciones son "+str(ecuacion.obtener_solucion()))