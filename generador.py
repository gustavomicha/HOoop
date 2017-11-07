"""
Un generador de senal es el responsable de generar una senal portadora.

"""

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds*self.frecuencia_muestreo

        muestras = range(cantidad_muestras)
        #TODO agregar un ruido blanco a la senal
        ruido = 0.1*self.amplitud*np.random.normal(size=len(muestras))

        ret = [self.amplitud*math.sin(self.frecuencia*i+self.fase) \
        for i in muestras]
	retruido = ret + ruido

        return retruido,ret,ruido
