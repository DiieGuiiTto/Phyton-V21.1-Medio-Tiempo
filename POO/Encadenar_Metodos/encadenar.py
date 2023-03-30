class Usuario:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.balance = saldo_inicial

    def hacer_retiro(self, amount):
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
            return self
        else:
            self.balance -= amount
            print("Retiro exitoso. Saldo restante:", self.balance)
            return self

    def mostrar_balance(self):
        print(self.nombre ,"tu saldo es :", self.balance)
        return self

    def hacer_deposito(self, amount):
        self.balance += amount
        print("Se ah Depositado con exito Saldo actual:", self.balance)   
        return self  

    def tranferencia(self, amount,user):
        
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
            return self
        else:
            self.balance -= amount
            user.balance += amount
            print("Tu transferencia hacia",user.nombre,"fue exitosa. Tu saldo es :", self.balance)
            return self


Pedro = Usuario("Pedro", 10000)
Juan = Usuario("Juan", 10000)
Diego = Usuario("Diego", 10000)

Pedro.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).hacer_retiro(400).mostrar_balance()
Juan.hacer_deposito(100).hacer_deposito(100).hacer_retiro(400).hacer_retiro(180).mostrar_balance()
Diego.hacer_deposito(300).hacer_retiro(100).hacer_retiro(100).mostrar_balance()
Juan.tranferencia(100, Diego).mostrar_balance()
Diego.mostrar_balance()