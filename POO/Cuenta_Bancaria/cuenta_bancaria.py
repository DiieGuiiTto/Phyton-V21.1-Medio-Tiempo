class CuentaBancaria:

    nombre_banco = "PrimerDojo"
    todas_las_cuentas = []
    def __init__(self, int_rate, balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)


@classmethod
def cambiar_nombre_de_banco(cls,name):
    cls.nombre_banco = name

@classmethod
def todos_los_balances(cls):
    sum = 0

    for account in cls.todas_las_cuentas:
        sum += balance.cuenta
        return sum
class CuentaBancaria:
    def re_tiro(self,amount):


        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance -= amount
        else:
            print("Fondos Insuficientes")
        return self
    
    def puede_retirar(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
class CuentaBancaria:
    def __init__ (  self, tasa.interes , balance ):
        pass