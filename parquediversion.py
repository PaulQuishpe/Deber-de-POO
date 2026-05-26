class Parque:

    def __init__(self, nombre, ciudad, capacidad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.capacidad = capacidad

    def abrir(self):
        print("Parque abierto")

    def mostrar(self):
        print("Nombre:", self.nombre)


class ParqueDiversion(Parque):

    def __init__(self, nombre, ciudad, capacidad, juegos):
        super().__init__(nombre, ciudad, capacidad)
        self.juegos = juegos

    def iniciar(self):
        print(
            f"Nombre:{self.nombre} ciudad:{self.ciudad}"
            f" capacidad:{self.capacidad} personas juegos:{self.juegos}"
        )

    def nuevo(self):
        print("Parque nuevo")


p1 = ParqueDiversion("Fantasy", "Quito", 500, 25)

p1.abrir()
p1.iniciar()
p1.nuevo()