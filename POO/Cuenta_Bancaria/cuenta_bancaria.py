class CuentaBancaria:

    nombre_banco = "PrimerDojo"
    def __init__(self, int_rate, balance):
        self.tasa_int = tasa_interes
        self.balance = balance
        self.name = name 
    def depositar(self, monto):
        self.balance += monto
        print(f"Se Ah Depositado {monto} a {self.name} Saldo Actual: {self.balance}")
        return self
    def retiro(self, monto):
        if monto > self.balance:
            self.balance -=5
            print("Saldo Insuficiente. Transaccion Fallida.")
            return self
        else:
            self.balance -= monto
            self.balance -=5
            print(f"Se Han Retirado {monto}, Saldo Actual Es {self.balance}")
            return self


    def info_cuenta(self):
        print(f"Tasa De Interes: {self.tasa_int}")
        print(f"Saldo Disponible: {self.balance}")
        return self