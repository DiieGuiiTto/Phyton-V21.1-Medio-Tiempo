class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email, apellido):
        self.name = name
        self.email = email
        self.apellido = apellido
        self.balance_cuenta = 0
    # agregando el método de depósito

    def hacer_depósito(self, monto):  # toma un argumento que es el monto del depósito
        self.balance_cuenta += monto

    def hacer_giro(self, monto):  # toma un argumento que es el monto del depósito
        # la cuenta del usuario específico aumenta en la cantidad del valor recibido
        self.balance_cuenta -= monto
        # la cuenta del usuario específico aumenta en la cantidad del valor recibido

    def mostrar_saldo(self):
        print(f"Mi saldo es: {self.balance_cuenta}")



devid = Usuario("David" , "david@gmail.com" ,"ponce")
diego = Usuario("Diego" ,"diego@gmail.com" ,"iturra")
dojo =Usuario("Coding" , "coding@dojo.cl" ,"dojo")




diego.hacer_depósito(10000)
diego.hacer_depósito(10000)
diego.hacer_depósito(10000)

diego.hacer_giro(15000)

devid.hacer_depósito(50000)
devid.hacer_depósito(100000)

devid.hacer_giro(75000)
devid.hacer_giro(2000)

dojo.hacer_depósito(1500000)

dojo.hacer_giro(250000)
dojo.hacer_giro(250000)

print(f"Saldo Diego: {diego.balance_cuenta}", f"Saldo David: {devid.balance_cuenta}", f"Saldo Dojo: {dojo.balance_cuenta}")


