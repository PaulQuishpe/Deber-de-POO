class Observatorio:

    def __init__(self, nombre, ubicacion, telescopios):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.telescopios = telescopios

    def abrir(self):
        print("Observatorio abierto")

    def mostrar(self):
        print("Nombre:", self.nombre)


class ObservatorioLunar(Observatorio):

    def __init__(self, nombre, ubicacion, telescopios, satelite):
        super().__init__(nombre, ubicacion, telescopios)
        self.satelite = satelite

    def observar(self):
        print(
            f"Nombre:{self.nombre} ubicación:{self.ubicacion}"
            f" telescopios:{self.telescopios} satélite:{self.satelite}"
        )

    def capturar(self):
        print("Capturando imagen")


o1 = ObservatorioLunar("SpaceLab", "Ecuador", 5, "LunarX")

o1.abrir()
o1.observar()
o1.capturar()