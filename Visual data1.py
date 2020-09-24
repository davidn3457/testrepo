# importando modulos necesarios
import numpy as np
import pandas as pd
from pydataset import data
import re

# librerías de visualizaciones
import seaborn as sns
import matplotlib.pyplot as plt 
from bokeh.io import output_notebook, show
#from bokeh.charts import Histogram, Scatter
import folium
import notebook

"""
bici = pd.read_csv('bicicletria.csv', sep=';')
bici.head()"""
"""
def coord(c):
    coor = re.findall(r'-?\d+\.\d{7}', c)
    coords = [float(s) for s in coor]
    return coords[::-1]

bici['WKT'] = bici['WKT'].apply(coord)

# filtramos solo las bicicleterías de palermo
bici_palermo = bici[bici.BARRIO == 'PALERMO'][['WKT', 'NOMBRE']]
"""
#mapa = folium.Map(location=[-34.588889, -58.430556], zoom_start=13)
m = folium.Map([41.8781, -87.6298], zoom_start=11)
m
"""for index, row in bici_palermo.iterrows():
    mapa.simple_marker(row['WKT'], 
                   popup=row['NOMBRE'], marker_color='red',
                   marker_icon='info-sign')"""
