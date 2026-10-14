from abc import ABC, abstractmethod

# Interfaces pequeñas, una por tarea
class Guardador(ABC):
    @abstractmethod
    def guardar(self, numero, total):
        ...


class Notificador(ABC):
    @abstractmethod
    def notificar(self, correo, total):
        ...


class GuardadorEnMemoria(Guardador):
    def __init__(self):
        self.datos = {}

    def guardar(self, numero, total):
        self.datos[numero] = total


class NotificadorConsola(Notificador): 
    def notificar(self, correo, total):
        print(f"Correo a {correo}: total {total}")