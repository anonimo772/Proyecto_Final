class Direccion:
    def __init__(self, calle, ciudad, codigo_postal):
        self.calle = calle
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, CP: {self.codigo_postal}"
