from model.transporteprogresivaprogresiva import TransporteProgresivaProgresiva
from model.transporteprogresivaregresiva import TransporteProgresivaRegresiva
from model.transporteregresivaprogresiva import TransporteRegresivaProgresiva
from model.transporteregresivaregresiva import TransporteRegresivaRegresiva


class FactoriaTransporte:
    @staticmethod
    def crear_edp(edp):
        if edp.progresion['tiempo'] == 1:
            if edp.progresion['espacio'] == 1:
                print('caso 1')
                return TransporteProgresivaProgresiva(edp)
            else:
                print('caso 2')
                return TransporteProgresivaRegresiva(edp)
        else:
            if edp.progresion['espacio'] == 1:
                print('caso 3')
                return TransporteRegresivaProgresiva(edp)
            else:
                print('caso 4')
                return TransporteRegresivaRegresiva(edp)

