"""
dashDeployment.py

An interactive app that allows the user to input a song,
artist, or album and get back their background spotify
data.

"""

# ---------------------------------------------
# 0: Package Import
import requests
import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output

# ---------------------------------------------
# 1: Unlocking API

# Staging credentials and URL
clientID = 'afc6efa8f7ee456b8c1f8bda66ddbda3'
clientSecret = '49aec50b3cd84b3383744bc20de20388'
authURL = 'https://accounts.spotify.com/api/token'
baseURL = 'https://api.spotify.com/v1/'

# Posting
authResponse = requests.post(authURL, {
    'grant_type':'client_credentials',
    'client_id':clientID,
    'client_secret':clientSecret
})

# Convert to json
authResponseData = authResponse.json()

# Saving token
accessToken = authResponseData['access_token']

# ---------------------------------------------
# 2: Data Import

# Formatting Track ID
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# Setting headers for request
headers = {
    'Authorization': 'Bearer {token}'.format(token=accessToken)
}

# Data retrieval with headers
songRequest = requests.get(baseURL + 'audio-features/' + track_id, headers=headers).json()

# ---------------------------------------------
# 3: Staging Dash App

# Style Sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Creating App
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Creating widgets
app.layout = html.Div([
    dcc.Markdown('''
    #### Interactive Spotify Dashboard
    ''',
    style={
        'textAlign':'left'
    }
    ),
    dcc.Input(
        id="Track ID",
        placeholder="Enter Track ID here",
        style={
            'textAlign':'center'
        }
    ),
    html.Div(id="out-all-types")
])

# ---------------------------------------------
# 3: App Call-backs

# Update the input
@app.callback(
    Output("out-all-types", "children"),
    [Input("Track ID", "value")]
)

def update_trackID(track_id_input):
    if track_id_input is not None:
        songRequest = requests.get(baseURL + 'audio-features/' + track_id_input, headers=headers).json()
        return songRequest['loudness']

if __name__ == '__main__':
    app.run_server(debug=True)
