import json

class SistemaEnvios:
    def __init__(self):
        self.clientes = []
        self.envios = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_envio(self, envio):
        self.envios.append(envio)

    def mostrar_envios(self):
        for envio in self.envios:
            print("="*30)
            print(envio)

    def guardar_datos(self, archivo="envios.json"):
        datos = [{
            "cliente": envio.cliente.nombre,
            "id": envio.cliente.id_cliente,
            "estado": envio.estado,
            "precio": envio.calcular_precio()
        } for envio in self.envios]
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)

    def ventas_por_tipo(self):
        express = sum(e.calcular_precio() for e in self.envios if isinstance(e.paquete, PaqueteExpress))
        estandar = sum(e.calcular_precio() for e in self.envios if isinstance(e.paquete, PaqueteEstandar))
        print(f"Total Ventas Express: ${express}")
        print(f"Total Ventas Estándar: ${estandar}")
