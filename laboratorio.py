class Laboratorio:

    def __init__(self, nombre, ubicacion, empleados):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.empleados = empleados

    def abrir(self):
        print("Laboratorio abierto")

    def mostrar(self):
        print("Nombre:", self.nombre)


class LaboratorioGenetico(Laboratorio):

    def __init__(self, nombre, ubicacion, empleados, especie):
        super().__init__(nombre, ubicacion, empleados)
        self.especie = especie

    def analizar(self):
        print(
            f"Nombre:{self.nombre} ubicación:{self.ubicacion}"
            f" empleados:{self.empleados} especie:{self.especie}"
        )

    def reporte(self):
        print("Generando reporte")


l1 = LaboratorioGenetico("BioLab", "Quito", 30, "Humano")

l1.abrir()
l1.analizar()
l1.reporte()