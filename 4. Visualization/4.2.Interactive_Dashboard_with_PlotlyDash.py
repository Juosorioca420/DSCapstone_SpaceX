import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

import dash
from dash import Dash, dcc, html, Input, Output, State, no_update


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Read the data into pandas dataframe
df =  pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv", 
                            encoding = "ISO-8859-1")

min_pl = df['Payload Mass (kg)'].min(); max_pl = df['Payload Mass (kg)'].max()


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Create a dash application
app1 = dash.Dash(__name__)
# Clear the layout and do not display exception untill callback gets executed
app1.config.suppress_callback_exceptions = True
# Application layout
app1.layout = html.Div( children= [ 
            # TITLE
            html.H1('SpaceX Launch Records',
            style= {'textAlign': 'center', 'color': '#00037a', 'font-size': 25.5} ),



            # Outer division for DROPDOWNS
            html.Div([
                # Dropdown 1 and label
                html.Div([
                    # Division for adding dropdown label
                    html.Div( [ html.H2('Launch Site:', style={'margin-right': '2em', 'color': '#00037a'}) ] ),

                    # Add the dropdown
                    dcc.Dropdown(id='input-site', 
                                options=[ {'label': 'All Sites', 'value': 'all'}, {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40' },
                                          {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'}, {'label': 'KSC LC-39A', 'value': 'KSC LC-39A' },
                                          {'label': 'VAFB SLC 4E', 'value': 'VAFB SLC-4E'}
                                        ],
                                value = 'all', searchable = True,

                                placeholder= 'Please select a Launch Site',
                                style = {'width' : '80%', 'padding' : '3px', 'font-size' : 18, 'textAlign' : 'center'}
                                )
                         ], style={'display':'flex'}
                    ),

                     ]),
            html.Br(),
            
            # Add  GRAPH
            # REVIEW: Empty division providing an id that will be updated during callback
            html.Div([ ], id= 'pie'),
            html.Br(),



            # Add SLIDER
            html.P('Payload [kg]'),
            dcc.RangeSlider( id = 'input-payload',  value = [min_pl, max_pl],
                             min = 0, max = 10000, step = 1000 ),

            # Add  GRAPH               
            html.Div( [ ], id= 'scatter')

                                 ]
                        )


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app1.callback( [Output('pie', 'children')], [Input('input-site', 'value')] )
def get_pie(site):
    if site == 'all': 
        fig = px.pie(df, names = 'Launch Site', values = 'class', title= 'Total Landing success by Launching Site')
    else:
        temp = df[ df['Launch Site'] == site ]
        name = temp['class'].unique().tolist()

        temp = temp.groupby('class').count()
        vals = [temp.iloc[0,0], temp.iloc[1,0]]
        
        print(vals, name)

        fig = px.pie(temp, names = name, values = vals, title= f'Total Launches - {site}')

    # REVIEW: Return dcc.Graph() component to the empty division
    return [dcc.Graph(figure = fig)]

@app1.callback( [Output('scatter', 'children')], [Input('input-site', 'value'), Input('input-payload', 'value')] )
def get_scatter(site, payload):
    if site == 'all': # Para series se usa &, no and.
        temp = df[ (df['Payload Mass (kg)'] <= payload[1]) & (df['Payload Mass (kg)'] >= payload[0]) ]
        fig = px.scatter(temp, x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category',
                         title= f'Payload between {payload[0]} and {payload[1]} - General')
        fig.update_layout( yaxis = dict( tickmode = 'linear', tick0 = 0, dtick = 1 ) )
    else:
        temp = df[ (df['Launch Site'] == site) & (df['Payload Mass (kg)'] <= payload[1]) & (df['Payload Mass (kg)'] >= payload[0]) ]
        fig = px.scatter(temp, x = 'Payload Mass (kg)', y = 'class', color = 'Booster Version Category',
                         title= f'Payload between {payload[0]} and {payload[1]} - {site}')
        fig.update_layout( yaxis = dict( tickmode = 'linear', tick0 = 0, dtick = 1 ) )
    
    return [dcc.Graph(figure = fig)]

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__ == '__main__':
    app1.run_server() # debug = True