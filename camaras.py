class Camara:

    def __init__(self, marca, color, resolucion):
        self.marca = marca
        self.color = color
        self.resolucion = resolucion

    def encender(self):
        print("Cámara encendida")

    def mostrar(self):
        print("Marca:", self.marca)


class CamaraSeguridad(Camara):

    def __init__(self, marca, color, resolucion, memoria):
        super().__init__(marca, color, resolucion)
        self.memoria = memoria

    def grabar(self):
        print(
            f"Marca:{self.marca} color:{self.color}"
            f" resolución:{self.resolucion} memoria:{self.memoria}"
        )

    def detectar(self):
        print("Movimiento detectado")


c1 = CamaraSeguridad("Sony", "Negro", "4K", "128GB")

c1.encender()
c1.grabar()
c1.detectar()