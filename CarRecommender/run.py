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
    data_vector = []
    if request.method == 'POST':
        for value in request.form.values():
            data_vector.append(float(value))
        
        for value,key in request.form.iteritems(): 
            print(value,key)
        
        d0 = data_vector[0]
        d1 = data_vector[1]
        
        data_vector.remove(d0)
        data_vector.remove(d1)
        
        data_vector.insert(0,d0)
        data_vector.insert(0,d1)
        
        print(data_vector)
    
        data = recomienda_20F(data_vector)
        #data = recomienda_20([1,1,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0])

        #return render_template('views.html',tables=[data.to_html(classes='female', bold_rows=True)],titles=['Recomendacion','coches'])

    
        return render_template('views.html',tables=[data.to_html()],titles=['Recomendacion'])
if __name__ == "__main__":
    app.run(debug=True)