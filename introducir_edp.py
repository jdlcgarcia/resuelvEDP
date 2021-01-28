from model.transporte import transporte

ecuacion = transporte()
ecuacion.pedir_datos()
print("La ecuación " + ecuacion.imprimir() + " ha sido guardada en base de datos")