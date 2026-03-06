def es_mayor_de_edad(edad : int)-> bool:
    if edad >= 18 :
      return True
    else:
       return False
edad_usuario: int = 20

if es_mayor_de_edad(edad_usuario):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")   
exit()
