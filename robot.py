class Robot:

    def __init__(self, marca, color, bateria):
        self.marca = marca
        self.color = color
        self.bateria = bateria

    def encender(self):
        print("Robot encendido")

    def mostrar(self):
        print("Marca:", self.marca)


class RobotLimpiador(Robot):

    def __init__(self, marca, color, bateria, potencia):
        super().__init__(marca, color, bateria)
        self.potencia = potencia

    def limpiar(self):
        print(
            f"Robot marca:{self.marca} color:{self.color}"
            f" bateria:{self.bateria} potencia:{self.potencia}"
        )

    def barrer(self):
        print("Barriendo piso")


r1 = RobotLimpiador("Xiaomi", "Blanco", "90%", "120W")

r1.encender()
r1.limpiar()
r1.barrer()