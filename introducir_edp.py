from model.Transporte import Transporte

ecuacion = Transporte()
ecuacion.pedir_datos()
print("La ecuación #" + str(ecuacion.get_id()) + " ha sido guardada en base de datos")
