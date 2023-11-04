import pandas as pd
from nutri_model import *
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)



stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets = stylesheets)
server = app.server

app.layout = html.Div(children = [html.Div(className='row', children=[
                                      html.Div([
                                              html.Div(dcc.Dropdown(id="solid/beverage",
                                                                    options=[{"label":"solid food", "value": "solid"},
                                                                             {"label":"beverages", "value": "drinks"}],
                                                                    multi=False,
                                                                    value=None,
                                                                    placeholder="Select the type of food"), className = 'three columns'),
                                              html.Div(dcc.Input(id="energy",
                                                                 type ="number" ,
                                                                 placeholder="Energy (in KJ)"), className = 'three columns'),
                                              html.Div(dcc.Input(id="fat",
                                                                 type ="number" ,
                                                                 placeholder="Saturated Fat (in g)"), className = 'three columns'),
                                              html.Div(dcc.Input(id="sugar",
                                                                 type ="number" ,
                                                                 placeholder="Total sugar (in g)"), className = 'three columns')
                                          ]),
                                      html.Div([
                                              html.Div(dcc.Input(id="salty",
                                                                 type ="number" ,
                                                                 placeholder="Sodium (in mg)"), className = 'three columns'),
                                              html.Div(dcc.Input(id="fruits",
                                                                 type ="number" ,
                                                                 placeholder="% Fruits/Vegetables"), className = 'three columns'),
                                              html.Div(dcc.Input(id="fiber",
                                                                 type ="number" ,
                                                                 placeholder="Dietary Fibers (in g)"), className = 'three columns'),
                                              html.Div(dcc.Input(id="protein",
                                                                 type ="number" ,
                                                                 placeholder="Protein (in g)"), className = 'three columns')
                                          ]),
                                      html.Div([
                                              html.Div(
                                                dcc.Graph(id="graph1", figure = {}, style = {'backgroundColor': '#000000'}, className = 'twelve columns')                                                )
                                               ]),

                                      html.Div([
                                              html.Div(
                                                dcc.Graph(id="graph2", figure = {}, style = {'backgroundColor': '#000000'}, className = 'twelve columns')                                                )
                                               ])

                                    ])
                                ])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
#@app.callback(
#    [Output(component_id='graph1', component_property='figure'),
#     Output(component_id='graph2', component_property='figure')],

#    [Input(component_id='solid/beverage', component_property='value'),
#     Input(component_id='energy', component_property='value'),
#     Input(component_id='sugar', component_property='value'),
#     Input(component_id='salty', component_property='value'),
#     Input(component_id='fiber', component_property='value'),
#     Input(component_id='protein', component_property='value')]
#)

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='graph1', component_property='figure'),
    Output(component_id='graph2', component_property='figure'),
    [Input(component_id='solid/beverage', component_property='value'),
     Input(component_id='energy', component_property='value'),
     Input(component_id='fat', component_property='value'),
     Input(component_id='sugar', component_property='value'),
     Input(component_id='salty', component_property='value'),
     Input(component_id='fruits', component_property='value'),
     Input(component_id='fiber', component_property='value'),
     Input(component_id='protein', component_property='value')]
)


def update_graph1(s_b, energy, fat, sugar, salty, fruit, fiber, protein):
  if s_b == None or energy == None or fat == None or sugar == None or salty == None or fruit == None or fiber == None or protein == None:
    return [{}, {}]

  Energy_score = energy_points(energy)
  Saturated_Fats_score = saturated_fat_points(fat)
  Total_sugar_score=total_sugar_points(sugar)
  Sodium_score=total_sodium_points(salty)
  Veggies_score = veggies_points(fruit)
  Fibre_score = fibres_points(fiber)
  Protien_score = protiens_points(protein)


  df = pd.DataFrame(columns = ['Points', 'Composition', 'Score'])
  # append rows to an empty DataFrame
  df = df.append({'Points' : 'Energy (kJ)', 'Composition' : energy, 'Score' : Energy_score},
          ignore_index = True)
   
  df = df.append({'Points' : 'Saturated Fats (g)', 'Composition' : fat, 'Score' : Saturated_Fats_score},
          ignore_index = True)
   
  df = df.append({'Points' : 'Total Sugar (g)', 'Composition' : sugar, 'Score' : Total_sugar_score},
          ignore_index = True)
   
  df = df.append({'Points' : 'Sodium (mg)', 'Composition' : salty, 'Score' : Sodium_score},
          ignore_index = True)

  df = df.append({'Points' : 'Fruits, Vegetables, Nuts or legumes (%)', 'Composition' : fruit, 'Score' : Veggies_score},
          ignore_index = True)

  df = df.append({'Points' : 'Fibre (non-starch polysaccharides) (g)', 'Composition' : fiber, 'Score' : Fibre_score},
          ignore_index = True)

  df = df.append({'Points' : 'Protien (g)', 'Composition' : protein, 'Score' : Protien_score},
          ignore_index = True)

  #df.to_excel('Dataset.xlsx', index = False)

  nutri_value = df['Score'].sum()

  sum_negative_points = Energy_score + Saturated_Fats_score + Total_sugar_score + Sodium_score
  if sum_negative_points <= -11 and Veggies_score < 5:
    nutri_value -= Protien_score




  #df.to_excel('Dataset.xlsx', index = False)

  if s_b == 'solid':
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = nutri_value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [-40, 15]},
                 'steps': [{'range': [-40, -19], 'color': "red"},
                           {'range': [-18, -11], 'color': "orange"},
                           {'range': [-10, -3], 'color': "yellow"},
                           {'range': [-2, 15], 'color': "green"}],
                 'bar': {'color':"black"}},
        title = {'text': "Nutri Value"}))

  elif s_b == 'drinks':
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = nutri_value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [-40, 15]},
                 'steps': [{'range': [-40, -10], 'color': "red"},
                           {'range': [-9, -6], 'color': "orange"},
                           {'range': [-5, -2], 'color': "yellow"},
                           {'range': [-1, 15], 'color': "lightgreen"}],
                 'bar': {'color':"black"}},
        title = {'text': "Nutri Value"}))

  bar_fig = px.bar(df, x = 'Points', y = 'Score')

  return fig, bar_fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)