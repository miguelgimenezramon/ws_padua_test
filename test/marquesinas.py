# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:47:14 2019

@author: mgimenez
"""

from test.consultas  import item, obtener_elementos_request

URL_DATA_POS = 'https://www.zaragoza.es/sede/servicio/urbanismo-infraestructuras/transporte-urbano/poste-autobus/tuzsa-'

def obtener_llegadas(elemento):
    llegadas = []
    try:
        destinos = elemento['destinos']
        if(destinos != None):
            for destino in destinos:
                print(destino.keys())
                f = lambda x:x not in ("linea", "destino")
                claves = list(filter(f, destino.keys()))
                valores = destino.values()
                llegadas.append(llegada.crear(valores[0], valores[1], valores))
    except: 
        print("No hemos recuperado los destinos solicitados")
    return llegadas

def obtener_marquesinas(id_marquesina):
    print(URL_DATA_POS + id_marquesina + ".json")
    elemento = obtener_elementos_request(URL_DATA_POS + id_marquesina + ".json")
    mi_marquesina = marquesina.crear(elemento['id'], elemento['title'], elemento['lastUpdated'])
    obtener_llegadas(elemento)
    # mi_marquesina.llegadas()
    return mi_marquesina

class llegada():
    """Clase que representa las distintas llegadas de lineas a una marquesina"""
    
    def __init__(self, linea, destino, tiempos):
         self.__linea = linea
         self.__destino = destino
         self.__tiempos = tiempos
         
    @classmethod
    def crear(cls, linea, destino, tiempos):
        return cls(linea, destino, tiempos)        

class marquesina(item):
    """Clase que representa un poste o marquesina en el sistema"""
    

    def __init__(self, id, title, time):
         super().__init__(id)
         self.__llegadas = []
         self.__title = title
         self.__time = time

         
    def actualizar_llegadas(self):
        """Actualiza su listado de lllegadas invocando al REST"""
        pass     
    
     
    @property
    def destinos(self):     
         return self.__autobuses
     
    @property
    def title(self):     
         return self.__title
     
    @property
    def time(self):     
        return self.__time
    
    @property
    def llegadas(self):     
        return self.__llegadas
    
    @llegadas.setter
    def llegadas(self, valor):
        self.__llegadas = valor
         
    @classmethod
    def crear(cls, id, title, time):
        return cls(id, title, time)     