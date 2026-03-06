# Este programa simula la base de datos de un concesionario usando listas y diccionarios.
# 1. Crear lista vacía
concesionario = []
# 2. Crear un bucle que se repite exactamente 3 veces
for S in range(3):
    print(f"Registro del vehiculo {S+1}")

    # 3. Pedir los datos al usuario
    marca = input("Ingrese la marca del carro: ")
    modelo = input("Ingrese el modelo del carro: ")
    precio = input("Ingrese el precio del carro: ")

    # 4: Crear un diccionario temporal
    Vehiculo = {
    "marca": marca,
    "modelo": modelo,
    "precio": precio
    }

    # 5. Guardar el dicionario creado en la lista
    concesionario.append(Vehiculo)

# 6. Crear un segundo bucle para mostrar el informe final 
print("--Informe final--")

for carro in concesionario:
    print(f"Vehículo registrado: Marca {carro['marca']}, "
          f"Modelo {carro['modelo']}, "
          f"Precio ${carro['precio']}")

exit()