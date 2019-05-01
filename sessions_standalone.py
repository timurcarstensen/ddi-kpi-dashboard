import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import functions as f

style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=style)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


session = f.readExcelFromFolder('excel', 'UserSession')

session[['userSession_endTime', 'userSession_startTime']] = session[['userSession_endTime', 'userSession_startTime']].astype('datetime64')
session['sessionTime'] = session['userSession_endTime'] - session['userSession_startTime']
session['Weekday'] = session['userSession_startTime'].dt.dayofweek
session = session.groupby('Weekday').size()

session = session.to_frame()








app.layout = html.Div(children=[
    html.H1(children='Bookseller Ningbo - Dashboard'),

    html.Div([
    html.H3('Page hits per Weekday'),
    dcc.Graph(
    id='testGraph',
    figure= go.Figure
        (
            data = 
            [
                {'x': session.index,'y': session[0], 'type':'bar', 'name': 'Sessions'},
            ],
            layout = go.Layout
            (
                title='', showlegend=True, barmode='group', margin=go.layout.Margin
                (
                    l=200,
                    r=200,
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
    ]) 
])
if __name__ == '__main__':
    app.run_server(debug=True)
