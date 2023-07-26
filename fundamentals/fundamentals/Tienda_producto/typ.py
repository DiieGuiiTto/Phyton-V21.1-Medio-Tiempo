class producto:
    def __init__(self, name, precio, cantidad):
        self.name = name
        self.precio = precio
        self.cantidad = cantidad

    def print_info(self):
        print(f"Nombre: {self.name}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")

    def actualizar_precio(self, amount):
        self.precio += amount

test = producto("Queso", 10000, 10)

test.print_info()
test.actualizar_precio(100)
test.print_info()
