import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import functions as f

style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=style)

order = f.readExcelFromFolder('excel', 'Order')
customer = f.readExcelFromFolder('excel', 'Customer')

customer = customer.rename(columns={'cus_ID':'customerID'}, inplace=False)

order = order.rename(columns={'order_customerID':'customerID'}, inplace=False)

order = order.merge(customer, on='customerID', how='outer')


orderM = len(order.loc[(order.cus_gender == 'M')])
orderF = len(order.loc[(order.cus_gender == 'F')])
orderNaN = len(order) - (orderM + orderF)

app.layout = html.Div(children=[
    html.H1(children='Bookseller Ningbo - Dashboard'),

    html.Div([
    html.H3('Customer Gender Data'),    
    dcc.Graph(
    id='testGraph',
    figure={
                'data': [{'labels': ['Male', 'Female', 'Unknown'],
                'values': [orderM, orderF, orderNaN],
                'type': 'pie'}],
                'layout': 
                {
                    'title': ''
                }
            } 
        ), 
    ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)

