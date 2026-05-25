class Drone:

    def __init__(self, marca, color, bateria):
        self.marca = marca
        self.color = color
        self.bateria = bateria

    def encender(self):
        print("Drone encendido")

    def mostrar(self):
        print("Marca:", self.marca)


class DroneAgricola(Drone):

    def __init__(self, marca, color, bateria, capacidad):
        super().__init__(marca, color, bateria)
        self.capacidad = capacidad

    def fumigar(self):
        print(
            f"Drone marca:{self.marca} color:{self.color}"
            f" bateria:{self.bateria} fumigando:{self.capacidad}")

    def medir(self):
        print("Midiendo humedad")


d1 = DroneAgricola("DJI", "Blanco", "80%", "10L")

d1.encender()
d1.fumigar()
d1.medir()