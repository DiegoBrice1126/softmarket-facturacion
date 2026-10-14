# Esta clase solo calcula el total
class Calculadora:
    IVA = 0.19

    def __init__(self, descuento):
        self.descuento = descuento

    def total(self, items):
        subtotal = sum(i["precio"] * i["cantidad"] for i in items)
        base = subtotal - self.descuento.calcular(subtotal)
        return round(base * (1 + self.IVA), 2)