import numpy as np
import math
import generador
import datetime

#puntos=[1,1,2,1]  
#ruido =np.random.normal(8,1,size=len(puntos))
#print(ruido)
#puntos=[1,1,2,1]
#forraro=[np.random.normal(0,1,1) for i in range(len(puntos))]
#print(forraro)


amplitud = 0.2
fase = 1
frecuencia = 2
frecuencia_muestreo = 3*frecuencia

def generar(tiempo_inicial, tiempo_final):
        cantidad_muestras = (tiempo_final - tiempo_inicial)*frecuencia_muestreo
        muestras = range(cantidad_muestras)
        ruido = 0.1*amplitud*np.random.normal(size=len(muestras))
        ret = [amplitud*math.sin(frecuencia*i+fase) for i in muestras]
	retruido = ret + ruido
        return ruido,ret,retruido
print(generar(1,2))
#print(ret)
