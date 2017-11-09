from flask import *
import pandas as pd
from flask import request
from recomendador import recomienda_20F

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('student.html')

@app.route("/result",methods = ['POST', 'GET'])
def result():
    
    #Variables locales
    data_vector = []
    data_vector_ord = []
    lista_ordenes = [1,2,11,14,6,5,13,0,10,12,8,4,15,9,3,16,7] 
    
    if request.method == 'POST':
        
        #Recuperacion de los params/datos del formulario
        for value in request.form.values():
            data_vector.append(float(value))

        #Ordenacion de los datos para poder ser calculadas las distancias 
        for orden in lista_ordenes:
            data_vector_ord.append(data_vector[orden])
        
        #Trazas
        print(data_vector)
        print(data_vector_ord)
    
        #Calculo de las recomendaciones
        data = recomienda_20F(data_vector_ord)

        return render_template('views.html',tables=[data.to_html(index=False)],titles=['Recomendacion'])
    
    
if __name__ == "__main__":
    app.run(debug=True)
