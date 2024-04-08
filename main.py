os.system(r"pip install dash")
os.system(r"pip install plotly.express")
os.system(r"pip install pandas")
from dash import Dash, dcc, html, Input, Output, State, dash_table
import plotly.express as px
import pandas as pd

df = px.data.iris()  # Sample dataset 
points_data = []  # Stores the submitted points

app = Dash(__name__, external_stylesheets=['styles.css'])
app.layout = html.Div(
    
    children=[
        html.H1("3D Graph Plotter", style={'textShadow': '2px 2px 4px rgba(0, 0, 0, 0.5)'}),
        html.H3("by aarikg", style={'textShadow': '2px 2px 4px rgba(0, 0, 0, 0.5)'}, className='electric-blue'),
        html.Div([  # Input section
            dcc.Input(id="x-input", type="number", placeholder="X coordinate"),
            dcc.Input(id="y-input", type="number", placeholder="Y coordinate"),
            dcc.Input(id="z-input", type="number", placeholder="Z coordinate"),
            html.Button('Submit Point', id='submit-button', n_clicks=0)
        ]),
        dcc.Graph(id="graph"),
        
    ]
)


@app.callback(
    Output("graph", "figure"),
    Output('x-input', 'value'),
    Output('y-input', 'value'),
    Output('z-input', 'value'),
    Input('submit-button', 'n_clicks'),
    State('x-input', 'value'),
    State('y-input', 'value'),
    State('z-input', 'value')
)
def update_graph_and_table(n_clicks, x, y, z):
    global points_data

    if n_clicks > 0:
        print(x)
        if x!="" or y!="" or z!="":
            points_data.append({'X': x, 'Y': y, 'Z': z})

        # Create a DataFrame for both plot and table
        plot_df = pd.DataFrame(points_data)
        

        fig = px.scatter_3d(
            plot_df,
            x="X",
            y="Y",
            z="Z",  # Color if 'species' exists
        )
        return fig, '', '', ''  # Clear inputs
    else:
        return px.scatter_3d(), '', '', ''  # Initial state

if __name__ == "__main__":
    app.run_server(debug=False)
