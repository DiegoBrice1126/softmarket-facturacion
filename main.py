"""Programa principal: arma las piezas, emite una factura y verifica el resultado."""
 
from descuentos import DescuentoPorcentual, SinDescuento
from calculadora import Calculadora
from servicio import ServicioFacturacion, GuardadorEnMemoria, NotificadorConsola
 
# Un ítem: 2 unidades a 50.000 -> subtotal de 100.000.
items = [{"precio": 50000, "cantidad": 2}]
 
# Se arman las piezas y se inyectan en el servicio (cliente mayorista: 10 %).
servicio = ServicioFacturacion(
    Calculadora(DescuentoPorcentual(0.10)),
    GuardadorEnMemoria(),
    NotificadorConsola(),
)
total = servicio.emitir("F-001", "cliente@correo.com", items)
 
# assert falla con error si la condición es falsa.
assert total == 107100.0  # (100000 - 10000) * 1.19
assert Calculadora(SinDescuento()).total(items) == 119000.0  # 100000 * 1.19
print("Pruebas OK")