import plotly.express as px
from dash import Dash, dcc, html, Input, Output,dash_table
import pandas  as pd
import dash_mantine_components as dmc
import plotly.graph_objects as go

df = pd.read_csv('./data.csv', sep=',', encoding='utf-8')
print(df)
app = Dash(__name__, title='Mi dash')



graficos = [
    'Grafico de barras',
    'Grafico de linea',
    'Grafico de pastel',
    'Grafico de dispersion',
]

app.layout = html.Div(
[
    html.Div(["Luis Avila", "IV",  dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in graficos ],
            id='my-dmc-radio-item',
            value='Grafico de barras',
            size="sm"
        ),  ], style={'flex': '1'}),
    html.Div([
        dcc.Graph(figure={}, id='graph-placeholder')
        ], style={'flex': '10'}, id= 'divprueba'),
 ],
style= {'width': '100%', 
        'height': '100vh',
        'display': 'flex'
        
        })


@app.callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)

def updateGraph(value):
    
    if value == 'Grafico de barras':
        return px.bar(df, x='Genero')
    if value == 'Grafico de linea':
        año2022= len(df[df['año'] ==  2022])
        año2023= len(df[df['año'] ==  2023])
        año2024= len(df[df['año'] ==  2024])
        
        return px.line(df, x=[ '2021', '2022', "2023", "2024"], y= [0,año2022, año2023, año2024])
    if value == 'Grafico de pastel':
        return px.pie(df, names='Preferencia de trabajo' )
    if value == 'Grafico de dispersion':
        dff= df[df['Genero'] ==  'Mujer']
        # dff['año'] = df['año'].astype(str) 
        return px.scatter(dff, x='año')
    
    

app.run_server( debug= True )





