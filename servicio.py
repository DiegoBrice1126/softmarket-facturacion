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


# El servicio recibe abstracciones, no clases concretas
class ServicioFacturacion:
    def __init__(self, calculadora, guardador, notificador):
        self.calculadora = calculadora
        self.guardador = guardador
        self.notificador = notificador

    def emitir(self, numero, correo, items):
        total = self.calculadora.total(items)
        self.guardador.guardar(numero, total)
        self.notificador.notificar(correo, total)
        return total