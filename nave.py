class Nave:

    def __init__(self, nombre, velocidad, combustible):
        self.nombre = nombre
        self.velocidad = velocidad
        self.combustible = combustible

    def despegar(self):
        print("Nave despegando")

    def mostrar(self):
        print("Nombre:", self.nombre)


class NaveEspacial(Nave):

    def __init__(self, nombre, velocidad, combustible, planeta):
        super().__init__(nombre, velocidad, combustible)
        self.planeta = planeta

    def explorar(self):
        print(
            f"Nave:{self.nombre} velocidad:{self.velocidad}"
            f" combustible:{self.combustible} destino:{self.planeta}"
        )

    def aterrizar(self):
        print("Aterrizando")


n1 = NaveEspacial("Apollo", "3000km", "95%", "Marte")

n1.despegar()
n1.explorar()
n1.aterrizar()