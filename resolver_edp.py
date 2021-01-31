from model.factoria_transporte import factoria_transporte
from model.transporte import transporte

ecuacion = transporte()
while True:

    try:
        id_ecuacion = int(input("Por favor, introduce el identificador de tu ecuación: "))
        break
    except ValueError:
        print("Error! El identificador introducido no es un número. Por favor, inténtelo de nuevo.")

if ecuacion.cargar(id_ecuacion):
    print("La ecuación a resolver es "+ecuacion.imprimir())
    factoria = factoria_transporte()
    ecuacion_tipo = factoria.crear_edp(ecuacion)
    ecuacion_tipo.evaluar()
    print("Su mallado es:\n")
    print(ecuacion.imprimir_matriz())
    print("Los puntos solución son:\n")
    print(ecuacion.imprimirPuntosSolucion())
