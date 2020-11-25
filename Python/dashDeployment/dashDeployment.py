"""
dashDeployment.py

Current Version: 1.1
    # Simple chart with artificial data. The user can select y axis.
    # Next Step: Incorporate a regression block of code
    # Last Updated: 11/22

"""

# ---------------------------------------------
# 0: Package Import
import pandas as pd
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import dash
import plotly.express as px
import scipy.stats

# ---------------------------------------------
# 1: Temp Data
temp_col1 = np.random.randint(10,40,400)
temp_col2 = 0.8*temp_col1
temp_col3 = np.random.randint(10,40,400)

temp_dict = {
    'Conversions':temp_col1,
    'Impressions':temp_col2,
    'Clicks':temp_col3
}

tempData = pd.DataFrame.from_dict(temp_dict)

# ---------------------------------------------
# 2 : Global Variables
    # Test
fig = px.scatter(tempData, x = 'Impressions', y = 'Conversions')


# ---------------------------------------------
# 3: Dash App Framework
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label':i, 'value':i} for i in list(tempData.columns)]
    ),
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),
    html.Div(id='dd-output-container')
])

# ---------------------------------------------
# 4: Dash App User Updates
@app.callback(
    dash.dependencies.Output('basic-interactions', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])

def update_graph(value):
    fig = px.scatter(tempData, x = 'Impressions', y = value)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)