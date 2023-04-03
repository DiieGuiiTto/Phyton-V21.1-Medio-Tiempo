class Mascota:

    def __init__(self, nombre , tipo, trucos, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.trucos = trucos
        self.health = 100
        self.energia = 50
        self.sonido = sonido

    def dormir(self):
        self.energia += 25
        return self


    def comer(self):
        self.energia += 5
        self.health += 10
        return self

    def jugar(self):
        self.health += 5
        self.energia -= 15
        return self

    def sonido(self):
        print(self.sonido)

class Ninja:

    def __init__(self, apellido, primer_nombre, golosinas, mascota_comida, Mascota):
        self.primer_nombre = primer_nombre
        self.apellido = apellido
        self.golosinas = golosinas
        self.comida_de_mascota = comida_de_mascota
        self.mascota = Mascota

    def walk(self):
        self.mascota.jugar()
        return self


    def feed(self):

        if len(self.mascota_comida) > 0:
            comida = self.mascota_comida.pop()
            print(f"Alimentacion {self.mascota.nombre} {comida}!")
            self.mascota.comer()
        else:
            print("¡¡¡Oh, no!!! ¡Necesitas más comida para mascotas!")
        return self

    def bathe(self):
        self.mascota.sonido()
golosinas = ['Salchicha','Cecina',"Bolsa de basura"]
comida_de_mascota = ['Pizza','Hamburguesa']

mordisco = Mascota("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

Lucho = Ninja("matias","Dion",golosinas, comida_de_mascota, mordisco)

Lucho.feed();
Lucho.feed();
Lucho.feed();