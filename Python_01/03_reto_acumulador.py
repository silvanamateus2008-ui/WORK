Acumulador = 0 
for S in range (5):
    precio = float(input(f"Ingrese el precio del producto {S + 1}: "))
    Acumulador = Acumulador + precio
print("El costo total de la compra es: ", Acumulador)

exit()