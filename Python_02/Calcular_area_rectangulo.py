def calcular_area_rectangulo (base : float, altura : float) -> float:
    """Calculando el area en el sistema"""
    area: float = base * altura
    return area
area_rectangulo: float = calcular_area_rectangulo (12.0,7.0)
print(f"El area del rectangulo es: {area_rectangulo}")