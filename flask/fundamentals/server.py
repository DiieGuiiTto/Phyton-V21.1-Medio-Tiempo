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
    return f"Hola mundo saluda {name}"



@app.route('/repetir/<int:num>/<string:palabra>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(num, palabra):
    salida = ''
    for i in range(0,num):
        salida += f"<p>{palabra}</p>"

    return salida

@app.errorhandler(404)
def error_pagina(error):
    return f"wowww no existe la página"


























# Devuelve la cadena '¡Hola Mundo!' como respuesta
if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)   


