from model.ecuacion import Ecuacion

ecuacion = Ecuacion()
ecuacion.cargar(2)
print("La ecuación a resolver es "+ecuacion.imprimir())
ecuacion.resolver()
print("La solución es "+str(ecuacion.obtener_solucion()))