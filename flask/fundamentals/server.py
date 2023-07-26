from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hola_mundo():
    return 'Hola Mundo!'

    
@app.route('/dojo')
def dojo():
  return "dojo"
    

@app.route('/hola/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def hola(name):
    print(name)
    return "Hola, " + name



@app.route('/repeat/num:int/<name>:string') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(repeat, num):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id




























# Devuelve la cadena '¡Hola Mundo!' como respuesta
if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)   


