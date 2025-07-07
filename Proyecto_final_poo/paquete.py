class Paquete:
    def __init__(self, peso, dimensiones, valor_base):
        self._peso = peso
        self._dimensiones = dimensiones
        self._valor_base = valor_base

    def calcular_precio(self):
        return self._valor_base

    def __str__(self):
        return f"Peso: {self._peso}kg, Dimensiones: {self._dimensiones}, Precio base: ${self._valor_base}"

class PaqueteEstandar(Paquete):
    def calcular_precio(self):
        return self._valor_base  # No cambia

class PaqueteExpress(Paquete):
    def __init__(self, peso, dimensiones, valor_base, recargo):
        super().__init__(peso, dimensiones, valor_base)
        self.__recargo = recargo

    def calcular_precio(self):
        return self._valor_base + self.__recargo
