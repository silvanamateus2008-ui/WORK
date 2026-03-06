def crear_perfil(nombre:str, rol:str) -> None:
    """Registra un nuevo perfil en el Sistema"""
    print(f"Registrando en base de datos : {nombre} | Permisos : {rol}")

crear_perfil("Carlos","Admin")
crear_perfil("Ana","Ventas")