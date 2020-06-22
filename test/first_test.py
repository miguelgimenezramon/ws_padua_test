#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:17:38 2020

@author: gloppert
"""

from threading import Thread
from time import sleep

class Measures:

    def __init__(self, path):
        self.__path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def temp(self, path):
        self.__path = path

    def __read_files(self):
        try:
            fichero = open(self.__path, 'rt')
            # print(fichero.readlines())
            # print(fichero.read())
            nuevo_fichero = open('C:/develop/pythonProjects/resources/change_new.txt', 'at')
            nuevo_fichero.write(fichero.read())

            nuevo_fichero.close()
            fichero.close()
        except BaseException as exec:
            print("Error al procesar el fichero:", exec)
            print("The file could not be opened:", strerror(exec.errno));



    def __start_weather_station(self):
        while True:
            measure = self.get_measures()
            self.__show_temp(int(measure.temp))
            sleep(15)
            self.__show_humidity(int(measure.humidity))
            sleep(15)

    def __start_capture_event(self):
        while True:
           for event in self.__sensehat.stick.get_events():
               if event.action == "pressed":
                   measure = self.get_measures()
                   if(not self.__temp):
                       self.__show_temp(int(measure.temp))
                   else:
                       self.__show_humidity(int(measure.humidity))
               sleep(0.5)








