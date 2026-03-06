class Vehiculo:
    def __init__(self, marca : str, modelo: str, anio: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.anio: int = anio 

vehiculo_1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo_2 = Vehiculo("Ford", "Mustang", 2022)

print(f"El vehículo: {vehiculo_1.marca} de modelo {vehiculo_1.modelo} y del año {vehiculo_1.anio}")
print(f"El vehículo: {vehiculo_2.marca} de modelo {vehiculo_2.modelo} y del año {vehiculo_2.anio}")
