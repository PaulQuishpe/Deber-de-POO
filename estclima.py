class Estacion:

    def __init__(self, ciudad, temperatura, humedad):
        self.ciudad = ciudad
        self.temperatura = temperatura
        self.humedad = humedad

    def medir(self):
        print("Midiendo clima")

    def mostrar(self):
        print("Ciudad:", self.ciudad)


class EstacionClimatica(Estacion):

    def __init__(self, ciudad, temperatura, humedad, viento):
        super().__init__(ciudad, temperatura, humedad)
        self.viento = viento

    def detectar(self):
        print(
            f"Ciudad:{self.ciudad} temperatura:{self.temperatura}"
            f" humedad:{self.humedad} viento:{self.viento}"
        )

    def registrar(self):
        print("Datos guardados")


e1 = EstacionClimatica("Quito", "20°", "60%", "15km")

e1.medir()
e1.detectar()
e1.registrar()