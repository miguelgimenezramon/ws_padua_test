# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:26:33 2019

@author: CTA
"""

import requests

def obtener_elementos_request(url):
    response = requests.get(url)
    resulset = response.json()
    return resulset

class item:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id
        
