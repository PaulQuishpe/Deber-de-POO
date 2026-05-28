class Traje:

    def __init__(self, color, material, peso):
        self.color = color
        self.material = material
        self.peso = peso

    def activar(self):
        print("Traje activado")

    def mostrar(self):
        print("Color:", self.color)


class TrajeEspacial(Traje):

    def __init__(self, color, material, peso, oxigeno):
        super().__init__(color, material, peso)
        self.oxigeno = oxigeno

    def verificar(self):
        print(
            f"Color:{self.color} material:{self.material}"
            f" peso:{self.peso} oxígeno:{self.oxigeno}"
        )

    def regular(self):
        print("Regulando temperatura")


t1 = TrajeEspacial("Blanco", "Titanio", "20kg", "100%")

t1.activar()
t1.verificar()
t1.regular()