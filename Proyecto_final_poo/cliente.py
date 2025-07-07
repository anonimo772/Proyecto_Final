from direccion import Direccion

class Cliente:
    def __init__(self, nombre, id_cliente, direccion: Direccion):
        self.__nombre = nombre
        self.__id_cliente = id_cliente
        self.__direccion = direccion

    def __str__(self):
        return f"{self.__nombre} - ID: {self.__id_cliente} - Dirección: {self.__direccion}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def id_cliente(self):
        return self.__id_cliente
