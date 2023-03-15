print("Hola,Mundo")

name = "Noelle"
print("Hola,", name)	
print("Hola," + name)	

name2 = "42"
print("Hola", name2)	
print("holaaaaaaaaaaaanda" + name2)  # Agregamos una coma después del string para concatenar con name2, que es un entero

fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}" .format(fave_food1,fave_food2))  # Agregamos {} para reemplazar con el valor de fave_food1
print(f"Amo comer {fave_food2} y {fave_food1}" ) # Eliminamos el argumento file ya que no es necesario y causaría un error sintáctico
