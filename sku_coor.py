## -*- coding: utf-8 -*-
#****************************************************************
#funciones para convertir a coordenadas celestes de coordenas x,y
#import matplotlib.pyplot as plt
#se usa wctool para realizar las conversiones
#****************************************************************
import os
#convierte un par de coordenadas x,y en una imagen a las coordenadas en el cielo
def convierte_2sky(x,y,nombre):
    ejecuta="xy2sky -n 2 -d "+nombre.replace("\n","")+" "+str(x)+" "+str(y)#me quede con presicion dos para recuperar la mayor parte de objetos
    salida=os.popen(ejecuta).readline().split()
    #print salida
    AR=salida[0]
    DEC=salida[1]
    return AR,DEC

#determina las coordenadas de un catalogo dado
def det_coordinates_catalog(nombre): #realiza la conversion de sistema de coordenadas
    ejecuta="gethead "+nombre.replace("\n","")+" RA DEC"
    salida=os.popen(ejecuta).readline().split()
    AR=salida[0]
    DEC=salida[1]
    ejecuta2="skycoor -d -n 1 "+AR+" "+DEC+" J2000"
    salida2=os.popen(ejecuta2).readline().split()
    AR=salida2[0]
    DEC=salida2[1]
    return AR,DEC

#Convierte las coordenadas daddas a el sistema de coordenadas con una presition de 6 decimales
def skycoor(AR,DECL):    

    ejecuta="skycoor -d -n 6 "+ str(AR)+" "+str(DECL)#me quede con presicion dos para recuperar la mayor parte de objetos
    print ejecuta
    salida=os.popen(ejecuta).readline().split()
    print salida
    if len(salida)>=2:
	    AR=salida[0]
	    DEC=salida[1]
    else:
	    AR=0
	    DEC=0
    return AR,DEC


