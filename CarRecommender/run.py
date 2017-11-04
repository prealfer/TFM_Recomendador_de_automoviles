from flask import *
import pandas as pd
from flask import request
from recomendador import recomienda_20

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('student.html')

@app.route("/result",methods = ['POST', 'GET'])
def result():
    
    if request.method == 'POST':
    
        #return render_template('result.html',result=request.form)
    
    #return render_template('result.html',result=result)
        data = recomienda_20([1,1,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0])
        #data = pd.read_csv('listado.csv').head()
      #data.set_index(['Name'], inplace=True)
      #data.index.name=None
      #females = data.loc[data.Gender=='f']
      #males = data.loc[data.Gender=='m']
        return render_template('views.html',tables=[data.to_html(classes='female')],titles=['na','coches'])
        #return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],titles = ['na', 'Female surfers', 'Male surfers'])

if __name__ == "__main__":
    app.run(debug=True)