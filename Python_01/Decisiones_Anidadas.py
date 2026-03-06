print("---Diagnóstico de red---")
hay_internet = input("¿el módem tiene luces encendidas? (si/no): ")
if hay_internet == "si":
    print("Paso 1: El equipo recibe energía.")
    Luz_roja = input("¿Alguna de las luces es color ROJO? (si/no): ")
    if Luz_roja == "si":
        print("Fallo detectado: Problema en la fibra óptica. Llame a soporte.")
    else:
        print("Todo normal: Su conexión está operando al 100%.")
else:
    print("Fallo critico: verifique que el equipo esté conectado a la corriente")
exit()



