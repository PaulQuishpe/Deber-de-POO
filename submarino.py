class Submarino:

    def __init__(self, nombre, profundidad, capacidad):
        self.nombre = nombre
        self.profundidad = profundidad
        self.capacidad = capacidad

    def sumergir(self):
        print("Submarino bajando")

    def mostrar(self):
        print("Nombre:", self.nombre)


class SubmarinoCientifico(Submarino):

    def __init__(self, nombre, profundidad, capacidad, laboratorio):
        super().__init__(nombre, profundidad, capacidad)
        self.laboratorio = laboratorio

    def analizar(self):
        print(
            f"Nombre:{self.nombre} profundidad:{self.profundidad}"
            f" capacidad:{self.capacidad} personas laboratorio:{self.laboratorio}"
        )

    def recolectar(self):
        print("Recolectando muestras")


s1 = SubmarinoCientifico("Titan", "5000m", 10, "Marino")

s1.sumergir()
s1.analizar()
s1.recolectar()