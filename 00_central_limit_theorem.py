# Import Dash components, plotly, and numpy
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

N_options = [10,100,1000,10000]

app = dash.Dash()

app.layout = html.Div([
    html.H2("Teorema Central del Límite - Ejemplo Binomial"),
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
    dcc.Graph(id='hgraph'),
])


@app.callback(
    dash.dependencies.Output('hgraph', 'figure'),
    [dash.dependencies.Input('N', 'value')])

def update_graph(N):
    trace = go.Histogram(x=np.random.randn(N))
    return {
        'data': [trace],
        'layout':
            go.Layout(title='Histograma {}'.format(N))
    }


if __name__ == '__main__':
    app.run_server(debug=True)
