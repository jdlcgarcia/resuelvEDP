from model.cuadratica import Cuadratica

ecuacion = Cuadratica()
ecuacion.pedir_datos()
print("La ecuación #" + str(ecuacion.get_id()) + " ha sido guardada en base de datos")
# ecuacion.cargar(1)
# print("La ecuación a resolver es "+ecuacion.imprimir())
# ecuacion.resolver()
# print("Las soluciones son "+str(ecuacion.obtener_solucion()))
