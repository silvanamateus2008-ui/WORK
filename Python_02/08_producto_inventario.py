class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int) -> None:
        try:
            if cantidad > self.stock:
                raise ValueError("Stock insuficiente")

            self.stock -= cantidad
            total = cantidad * self.precio

            print(f"Venta realizada: {cantidad} unidad(es) de {self.nombre}")
            print(f"Total a pagar: ${total}")
            print(f"Stock restante: {self.stock}")

        except ValueError as e:
            print(f" No se pudo realizar la venta de {self.nombre}: {e}")


class ProductoPerecedero(Producto):

    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int):
        super().__init__(nombre, precio, stock)
        self.dias_vencimiento = dias_vencimiento


producto1 = Producto("Laptop", 1200.0, 5)
producto2 = Producto("Mouse", 25.0, 10)
producto3 = ProductoPerecedero("Leche", 2.5, 20, 7)

producto1.vender(2)
producto2.vender(5)
producto3.vender(4)

producto1.vender(10)
producto3.vender(30)