import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

N_options = [10,100,1000]

app = dash.Dash()

app.layout = html.Div([
    html.H2("Teorema Central del Límite"),
    html.Div(
        [
            dcc.Dropdown(
                id="N",
                options=[{
                    'label': i,
                    'value': i
                } for i in N_options],
                value=''),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('N', 'value')])

def update_graph(N):

    trace = go.Histogram(x=np.random.randn(10))

    return {
        'data': [trace],
        'layout':
            go.Layout(title='Histograma {}'.format(N))
    }


if __name__ == '__main__':
    app.run_server(debug=True)
