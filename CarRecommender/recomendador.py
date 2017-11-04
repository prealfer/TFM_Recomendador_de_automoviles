
# coding: utf-8

# In[1]:

from scipy.spatial import distance
import pandas as pd



# In[18]:

normalizada = pd.read_csv('normalizado.csv')
normalizada.drop('Unnamed: 0',axis=1,inplace=True)

df_listado = pd.read_csv('listado.csv')
df_listado.drop('Unnamed: 0',axis=1,inplace=True)

array_norm = normalizada.values

def recomienda_20(_list):

    recorrido = range(len(normalizada))
    distancias = []

    for i in recorrido:
        distancias.append(distance.euclidean(_list, array_norm[i]))
        
    df_dist = pd.DataFrame({'dist':distancias, 'ind':recorrido})
    
    return df_listado.ix[df_dist.sort_values('dist', ascending=True).head(20).index]


# In[ ]:



