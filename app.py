#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 07:17:33 2022

@author: sof
"""
import pandas as pd
#import matplotlib.pyplot as plt
from dash import Dash, html, dcc
import plotly.express as px


app= Dash(__name__)

#cargar los datos 
#plt.close("all")
df=pd.read_excel('obesidad.xlsx',sheet_name = 0,names=["altura","peso","obeso"])
df.info()

fig=px.scatter(df,x="altura",y="peso",color="obeso")
app.layout = html.Div([html.H1('Altura vs. peso y la obesidad'),
            html.Div('Esta grafica muestra la comparacion entre la altura y el peso de una persona. Si es azul es que no es obesa y si es amarilla es que si es obesa'),
            dcc.Graph(
                id="graph",
                figure=fig
            )])

app.run_server(debug=True,host='0.0.0.0')
