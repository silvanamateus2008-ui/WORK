dias_semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
numero = (int(input("Escribe un numero del 1 al 7: ")))
if 1<= numero <=7:
    print(f"El dia correspondiente es: {dias_semana[numero-1]}")
else:
    print("El numero esta fuera de rango")
dias_semana.append("Otro dia")