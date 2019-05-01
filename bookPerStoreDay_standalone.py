import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import functions as f

style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=style)

order = f.readExcelFromFolder('excel', 'Order')

order = order.filter(['order_date', 'order_ID', 'order_location'], axis=1)
order['Weekday'] = order['order_date'].dt.dayofweek
order = order.groupby(['order_location', 'Weekday']).size()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


app.layout = html.Div(children=[
    html.H1(children='Bookseller Ningbo - Dashboard'),

    dcc.Graph(
    id='testGraph',
    figure=go.Figure
        (
            data = 
            [
                {'y': order[1], 'type':'bar', 'name': 'Store 1'},
                {'y': order[2], 'type':'bar', 'name': 'Store 2'},
                {'y': order[3], 'type':'bar', 'name': 'Store 3'},
                {'y': order[4], 'type':'bar', 'name': 'Online Store'}
                         
            ],
            layout = go.Layout
            (
                title='', showlegend=True, barmode='group', margin=go.layout.Margin
                (
                    l=50,
                    r=50,
                    b=50,
                    t=50,
                    pad=4
                ),
                xaxis= go.layout.XAxis
                (
                    tickmode = 'array',
                    tickvals = [0, 1, 2, 3, 4, 5, 6],
                    ticktext = weekdays
                )
            )
        )
    ), 
])
if __name__ == '__main__':
    app.run_server(debug=True)
