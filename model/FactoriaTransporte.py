from model.TransporteProgresivaProgresiva import TransporteProgresivaProgresiva
from model.TransporteProgresivaRegresiva import TransporteProgresivaRegresiva
from model.TransporteRegresivaProgresiva import TransporteRegresivaProgresiva
from model.TransporteRegresivaRegresiva import TransporteRegresivaRegresiva


class FactoriaTransporte:
    @staticmethod
    def crear_edp(edp):
        if edp.progresion['tiempo'] == 1:
            if edp.progresion['espacio'] == 1:
                return TransporteProgresivaProgresiva(edp)
            else:
                return TransporteProgresivaRegresiva(edp)
        else:
            if edp.progresion['espacio'] == 1:
                return TransporteRegresivaProgresiva(edp)
            else:
                return TransporteRegresivaRegresiva(edp)

