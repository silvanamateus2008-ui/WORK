colores = ["rojo","azul","verde"]
print(f"Lista de colores actual: {colores}")
color_eliminar = input("Escribe el color que no te guste").strip().lower()
if color_eliminar in colores:
    colores.remove(color_eliminar)
    print(f"Lista de colores actual: {colores}")
else:
    print("Ese color no esta en la lista")
exit()