"""
dashDeployment.py

Current Live: 1.2
    # Simple scatter plot of modeled data
    # User can update the target parameter in the regression
    # Next steps:
        - Visual enhancements to dashboard itself
        - Dynamically update x and y axis labels
        - Print out simple regression parameters
    # Last Updated: 11/24

"""

# ---------------------------------------------
# 0: Package Import

"""
Goal:
- Import basic functions
"""

import dash_core_components as dcc
import dash_html_components as html
import dash
import plotly.express as px
import scipy.stats as stats
import seaborn as sns
import statsmodels.api as sm

# ---------------------------------------------
# 1: Temp Data
"""
Pull in sample data to stage regression
"""

irisData = sns.load_dataset('iris')

# ---------------------------------------------
# 2: Functions and Variables
"""
Configure and stage global functions and variables to be used in the Dash app
"""

slope, intercept, r_value, p_value, std_err = stats.linregress(irisData['sepal_width'], irisData['sepal_length'])

reg_plot = px.scatter(irisData['sepal_width'],
                      intercept + irisData['sepal_length']*slope,
                      width=800,
                      height=400,
                      )

# ---------------------------------------------
# 3: Dash App

"""
Configure app settings, app layout
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown('''
    #### Interactive Regression Dashboard
    '''
    ),
    dcc.Dropdown(
        id='xAxis-dropdown',
        options=[{'label':i, 'value':i} for i in list(irisData.columns)]
    ),
    dcc.Graph(
        id='regression-figure',
        figure=reg_plot,
    ),
    html.Div(id='dd-output-container')
])

# ---------------------------------------------
# 4: Dash App User Updates

"""
Define decorators and functions to update chart based on user input
"""

@app.callback(
    dash.dependencies.Output('regression-figure', 'figure'),
    [dash.dependencies.Input('xAxis-dropdown', 'value')])

def update_graph(value):
    slope, intercept, r_value, p_value, std_err = stats.linregress(irisData['sepal_width'], irisData[value])
    reg_plot = px.scatter(irisData['sepal_width'],
                          intercept + irisData['sepal_width'] * slope,
                          width=800,
                          height=400,
                          )
    return reg_plot

if __name__ == '__main__':
    app.run_server(debug=True)
