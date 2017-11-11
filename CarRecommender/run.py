from flask import *
import pandas as pd
from flask import request
from recomendador import recomienda_20F
import seaborn as sns
import StringIO
import base64
import matplotlib.pyplot as plt

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
        
        img = StringIO.StringIO()
        
        plot = sns.barplot(data.modelo.map(lambda x: x.decode('unicode-escape')), data.precio)
        plot.set(xlabel='Vehiculos', ylabel='Precio')
        
        plt.savefig(img, format='png')
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue())

        return render_template('views.html',tables=[data.to_html(index=False)],titles=['Recomendacion'],plot_url=plot_url)
    
    
@app.route("/simple.png")
def simple():

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
