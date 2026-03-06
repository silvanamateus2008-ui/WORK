def calcular_salario_neto (salario_base: float, bonificacion: float = 0.0)-> float:
   descuento_salud_pension : float = salario_base * 0.08
   salario_final : float = salario_base - descuento_salud_pension + bonificacion 
   return salario_final 
resultado = calcular_salario_neto(100000.0,4000.0)
print(f"el salario neto es: {resultado}")

