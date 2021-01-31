from model.transporte_progresiva_progresiva import transporte_progresiva_progresiva
from model.transporte_progresiva_regresiva import transporte_progresiva_regresiva
from model.transporte_regresiva_progresiva import transporte_regresiva_progresiva
from model.transporte_regresiva_regresiva import transporte_regresiva_regresiva


class factoria_transporte:
    @staticmethod
    def crear_edp(edp):
        if edp.progresion['tiempo'] == 1:
            if edp.progresion['espacio'] == 1:
                print('caso 1')
                return transporte_progresiva_progresiva(edp)
            else:
                print('caso 2')
                return transporte_progresiva_regresiva(edp)
        else:
            if edp.progresion['espacio'] == 1:
                print('caso 3')
                return transporte_regresiva_progresiva(edp)
            else:
                print('caso 4')
                return transporte_regresiva_regresiva(edp)

