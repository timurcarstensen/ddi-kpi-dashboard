# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import functions as f
import pandas as pd
import revenueAndExpensesFeeder as rE
import bookPerStoreDayFeeder as bPSD
import sessionsFeeder as ss
import customerDemographicsFeeder as cD

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=style)


app.layout = html.Div(children=[
    html.H1(children='Bookseller Ningbo - KPI Dashboard'),

    html.Div([
        html.Div([
            html.H3(''),
            dcc.Graph(
        id='g1',
        figure = go.Figure
        (
            data = 
            [
                {'x': rE.mergeFrame['date'], 'y': rE.mergeFrame['invTotal'].values, 'type':'bar', 'name': 'Utilties and other Expenses'},
                {'x': rE.mergeFrame['date'], 'y': rE.mergeFrame['bookOrder_total'].values, 'type':'bar', 'name': 'Sales Revenue'},
                {'x': rE.mergeFrame['date'], 'y': rE.mergeFrame['sO_total'].values, 'type':'bar', 'name': 'Book Order Expense'}      
            ],
            layout = go.Layout
            (
                title='Revenue & Expenses'
            )
        )
    )
        ], className="six columns"),

        html.Div([
            html.H3(''),
            dcc.Graph(
        id='g2',
        figure = go.Figure
        (
            data = 
            [
                {'y': bPSD.order[1], 'type':'bar', 'name': 'Store 1'},
                {'y': bPSD.order[2], 'type':'bar', 'name': 'Store 2'},
                {'y': bPSD.order[3], 'type':'bar', 'name': 'Store 3'},
                {'y': bPSD.order[4], 'type':'bar', 'name': 'Online Store'}
                         
            ],
            layout = go.Layout
            (
                title='Revenue & Expenses', showlegend=True, barmode='group', margin=go.layout.Margin
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
    )
        ], className="six columns"),
    ], className="row"),


    html.Div([
        html.Div([
            html.H3(''),
            dcc.Graph(
        id='g3',
        figure = go.Figure
        (
            data = 
            [
                {'x': ss.session.index,'y': ss.session[0], 'type':'bar', 'name': 'Sessions'},
            ],
            layout = go.Layout
            (
                title='Website traffic per Weekday', showlegend=True, barmode='group', margin=go.layout.Margin
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
    )
        ], className="six columns"),

        html.Div([
            html.H3(''),
            dcc.Graph(
        id='g4',
        figure = {
                'data': [{'labels': ['Male', 'Female', 'Unknown'],
                'values': [cD.orderM, cD.orderF, cD.orderNaN],
                'type': 'pie'}],
                'layout': 
                {
                    'title': 'Customer Gender Data'
                }
            }    
    )
        ], className="six columns"),
    ], className="row"),
  
])

if __name__ == '__main__':
    app.run_server(debug=True)