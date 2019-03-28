import unittest
import math
import numpy as np

class complejo():
    def __init__(self,imaginario,real,norma):
        self.imaginario =imaginario
        self.real = real
        a=self.imaginario
        b=self.real
        r=((a**2)+(b**2))**(0.5)
        self.norma=r
        
    def conjugado(self):
        self.imaginario = -(self.imaginario)
    
     def calcula_norma(self):
        a=self.imaginario
        b=self.real
        r=((a**2)+(b**2))**(0.5)
        self.norma=r
    
    def pow(self):
        a=self.imaginario
        b=self.real
