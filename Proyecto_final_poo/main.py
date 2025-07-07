from direccion import Direccion
from cliente import Cliente
from paquete import PaqueteEstandar, PaqueteExpress
from envio import Envio
from sistema_envios import SistemaEnvios

sistema = SistemaEnvios()

while True:
    print("\n📦 MENÚ PRINCIPAL 📦")
    print("1. Registrar cliente")
    print("2. Crear envío")
    print("3. Ver envíos")
    print("4. Guardar en archivo")
    print("5. Mostrar ventas por tipo")
    print("6. Salir")
    opc = input("Seleccione opción: ")

    if opc == "1":
        nombre = input("Nombre: ")
        id_cliente = input("ID cliente: ")
        calle = input("Calle: ")
        ciudad = input("Ciudad: ")
        cp = input("Código postal: ")
        direccion = Direccion(calle, ciudad, cp)
        cliente = Cliente(nombre, id_cliente, direccion)
        sistema.registrar_cliente(cliente)
        print("Cliente registrado ✅")

    elif opc == "2":
        id_cliente = input("ID del cliente: ")
        cliente = next((c for c in sistema.clientes if c.id_cliente == id_cliente), None)
        if not cliente:
            print("❌ Cliente no encontrado.")
            continue
        tipo = input("Tipo de paquete (1. Estandar / 2. Express): ")
        peso = float(input("Peso (kg): "))
        dimensiones = input("Dimensiones: ")
        valor_base = float(input("Valor base: "))
        if tipo == "1":
            paquete = PaqueteEstandar(peso, dimensiones, valor_base)
        else:
            recargo = float(input("Recargo: "))
            paquete = PaqueteExpress(peso, dimensiones, valor_base, recargo)
        envio = Envio(cliente, paquete)
        sistema.crear_envio(envio)
        print("Envío creado ✅")

    elif opc == "3":
        sistema.mostrar_envios()

    elif opc == "4":
        sistema.guardar_datos()
        print("Datos guardados en JSON 📁")

    elif opc == "5":
        sistema.ventas_por_tipo()

    elif opc == "6":
        break
