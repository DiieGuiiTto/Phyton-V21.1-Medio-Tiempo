class Usuario:		
    def __init__(self, name, email, apellido):
        self.name = name
        self.email = email
        self.apellido = apellido
        self.balance_cuenta = 0

    def hacer_depósito(self, monto): 
        self.balance_cuenta += monto

    def hacer_giro(self, monto):  
        self.balance_cuenta -= monto

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


