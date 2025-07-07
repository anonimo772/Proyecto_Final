class Envio:
    def __init__(self, cliente, paquete):
        self.cliente = cliente
        self.paquete = paquete
        self.estado = "Pendiente"

    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def calcular_precio(self):
        return self.paquete.calcular_precio()

    def __str__(self):
        return f"{self.cliente}\nPaquete: {self.paquete}\nEstado: {self.estado}\nPrecio total: ${self.calcular_precio()}"
