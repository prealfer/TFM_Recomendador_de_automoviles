
# coding: utf-8

# # Recomendador de vehículos: Ejecución Back, del lado del servidor.

# In[20]:

from scipy.spatial import distance
import pandas as pd



# ## Inicialización de variables necesarias 

# In[21]:

normalizada = pd.read_csv('normalizado.csv')
normalizada.drop('Unnamed: 0',axis=1,inplace=True)

df_listado = pd.read_csv('listado.csv')
df_listado.drop('Unnamed: 0',axis=1,inplace=True)

md = ['LEON','IBIZA','GOLF','CORSA','MEGANE','POLO','CLIO','QASHQAI','SANDERO','308','C4','FOCUS','208','ASTRA','CAPTUR','TUCSON','AURIS','SPORTAGE','MOKKA','2008']
array_norm = normalizada.values

recorrido = range(len(normalizada))
index_tops=[]

for i in recorrido:
    if df_listado.iloc[i].modelo in md:
        index_tops.append(i)
    else:
        pass
    


# ## Método que recomienda 20 vehículos segun contenido sugerido por el usuario, sin filtrar por precios. 

# In[22]:

def recomienda_20(_list):

    recorrido = range(len(normalizada))
    distancias = []

    for i in recorrido:
        distancias.append(distance.euclidean(_list, array_norm[i]))
        
    df_dist = pd.DataFrame({'dist':distancias, 'ind':recorrido})
    
    return df_listado.ix[df_dist.sort_values('dist', ascending=True).head(20).index]


# ## Método que recomienda 20 vehículos segun contenido sugerido por el usuario, filtrando por el presupuesto disponible:
# 
# ### Argumentos de entrada: Lista de 17 valores, 16 normalizados y un presupuesto sin normalizar.

# In[26]:

def recomienda_20F(_list):

    recorrido = range(len(normalizada))
    distancias = []
    presupuesto_normalizado = (_list[0] - df_listado.precio.min())/(df_listado.precio.max()-df_listado.precio.min())
    presupuesto_maximo = (_list[0] + (2*_list[0])/10)
    presupuesto_minimo = (_list[0] - (3*_list[0])/10)
    _list.remove(_list[0])
    _list.insert(0,presupuesto_normalizado)
    
    for i in recorrido:
        if i in index_tops:
            distancias.append(distance.euclidean(_list, array_norm[i])-0.07)
        else:
            distancias.append(distance.euclidean(_list, array_norm[i]))
        
    df_dist = pd.DataFrame({'dist':distancias, 'ind':recorrido})
    df_recommend = df_listado.iloc[df_dist.sort_values('dist', ascending=True).index]
    
    return df_recommend[(df_recommend['precio']<presupuesto_maximo)&(df_recommend['precio']>presupuesto_minimo)].head(20)


# ## Método que devuelve las 20 menos distancias y su índice en la matriz total. 

# In[27]:

def top_distancias_20(_list):

    recorrido = range(len(normalizada))
    distancias = []
    presupuesto_normalizado = (_list[0] - df_listado.precio.min())/(df_listado.precio.max()-df_listado.precio.min())
    presupuesto_maximo = (_list[0] + (2*_list[0])/10)
    presupuesto_minimo = (_list[0] - (3*_list[0])/10)
    _list.remove(_list[0])
    _list.insert(0,presupuesto_normalizado)
    
    for i in recorrido:
        distancias.append(distance.euclidean(_list, array_norm[i]))
        
    df_dist = pd.DataFrame({'dist':distancias, 'ind':recorrido})
    
    return df_dist.sort_values('dist', ascending=True).head(20)

