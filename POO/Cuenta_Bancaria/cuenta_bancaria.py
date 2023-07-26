class CuentaBancaria:
    def __init__(self, int_rate, balance):
        self.tasa_int = int_rate
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Se Ah Depositado {monto} Saldo Actual: {self.balance}")
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

class Usuario:

    def __init__(self, name, email, int_tasa ,balan):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(int_rate=int_tasa,balance=balan)







diego = Usuario("Diego" ,"diego@gmail.com" ,int_tasa = 0.2 ,balan=2000 )
cristofer = Usuario("Cristofer","cristofer@gmail.com", int_tasa= 0.2, balan=2000)

diego.cuenta.depositar(1000).depositar(1000).depositar(1000).retiro(1500).info_cuenta()
cristofer.cuenta.depositar(1000).depositar(1000).retiro(200) .retiro(200) .retiro(200) .retiro(200).info_cuenta()