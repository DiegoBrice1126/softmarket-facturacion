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