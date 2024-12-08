from flask import Flask , render_template

import mysql.connector

connection = mysql.connector.connect(host = 'localhost',port = '3306', username ='root', database = 'CINE' , password = '111')

cursor = connection.cursor()



app = Flask(__name__)
@app.route("/")  

def index ():
  return render_template("index.html") 
  

@app.route("/registration")
def reg():
  return "detalles de l registro"
  
@app.route("/personita")
def Persona():
  cursor.execute("select * from Persona where genero ='Masculino' ")
  value = cursor.fetchall()
  return render_template("registration.html" , data = value , name= 'Persona')


@app.route("/pelicula")
def regi():
  return "Acontinuacion detalles de la pelicula (puedes borrar esta funcion )"

@app.route("/peliculita")
def Pelicula():
  cursor.execute("select * from Pelicula ")
  value = cursor.fetchall()
  return render_template("pelicula.html" , data = value , name= 'PELICULA')
  
  
@app.route("/procedimiento1/<int:codigo_actor>")
def Procedimiento1(codigo_actor):
    try:
        # Llamar al procedimiento almacenado
        cursor.callproc('ObtenerPeliculasPorActor', [codigo_actor])

        # Recuperar resultados
        results = []
        for result in cursor.stored_results():
            results = result.fetchall()

        # Renderizar los datos en una plantilla
        return render_template("procedimiento1.html", data=results, actor_id=codigo_actor)

    except mysql.connector.Error as e:
        return f"Error al ejecutar el procedimiento almacenado: {e}"

    
  
if __name__ == "__main__":
  app.run(debug=True)

