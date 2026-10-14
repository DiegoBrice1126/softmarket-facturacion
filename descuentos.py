"""Integrantes: Diego Briceño
Fecha: 13/10/2026 (DD/MM/YYYY)
SoftMarket S.A. - Buenas Practicas de Desarrollo de Software
Ejecutar: python anexo_a_codigo_solid.py
"""
from abc import ABC, abstractmethod
#Clases y demas explicados en el archivo PDF

class Descuento(ABC):
    @abstractmethod
    def calcular(self, subtotal):
        """Devuelve un valor entre 0 y subtotal."""


class SinDescuento(Descuento):
    def calcular(self, subtotal):
        return 0