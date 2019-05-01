import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import functions as f

style = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=style)

eNO = f.readExcelFromFolder('excel', 'ExpensesNonOrder')
supplierOrder = f.readExcelFromFolder('excel', 'SupplierOrder')
inv = f.readExcelFromFolder('excel', 'Invoice')
order = f.readExcelFromFolder('excel', 'Order')
BookOrder = f.readExcelFromFolder('excel', 'BookOrder')
Books = f.readExcelFromFolder('excel', 'Books')


Books = Books.filter(['book_ID', 'book_salesPrice']).rename(columns={"book_ID": "id", "book_salesPrice": "price"}, inplace=False)
BookOrder = BookOrder.rename(columns={"bookOrder_bookID": "id", "bookOrder_quantity": "quantity"}, inplace=False).merge(Books, on = 'id').rename(columns={'bookOrder_orderID':'orderID'}, inplace=False)


BookOrder = BookOrder.merge(order.filter(['order_ID', 'order_date']).rename(columns={'order_ID':'orderID', 'order_date':'date'}, inplace=False), on='orderID')
BookOrder[['quantity', 'price']] = BookOrder[['quantity', 'price']].astype(float)
BookOrder['bookOrder_total'] = BookOrder['quantity'] * BookOrder['price']

eNO = eNO.rename(columns={'exp_invoiceID':'invID'}, inplace=False)
eNO[['exp_date']] = eNO[['exp_date']].astype('datetime64')
eNOInv = eNO.merge(inv.rename(columns={'invoice_ID':'invID', 'invoice_amount':'invTotal'}, inplace=False), on = 'invID')
eNOInv = eNOInv.rename(columns={'exp_date':'date'}, inplace=False)


supplierOrder = supplierOrder.rename(columns={'sO_bookID':'id', 'sO_datetime': 'date'}, inplace=False)#['date'].astype('datetime64')
supplierOrder[['date']] = supplierOrder[['date']].astype('datetime64')
supplierOrder = supplierOrder.merge(Books, on = 'id')
supplierOrder['sO_total'] = (supplierOrder['sO_bookAmount'] * supplierOrder['price']).abs()*-1



days = pd.date_range(order['order_date'].min(), order['order_date'].max(), freq='D')
mergeFrame = days.to_frame(index=False)
mergeFrame = mergeFrame.rename(columns={0:'date'}, inplace=False)



mergeFrame = mergeFrame.merge(supplierOrder, on='date', how='outer')
mergeFrame = mergeFrame.merge(eNOInv, on='date', how='outer')
mergeFrame = mergeFrame.merge(BookOrder, on='date', how='outer')
mergeFrame = mergeFrame.filter(['date', 'sO_total', 'invTotal', 'bookOrder_total']) 




app.layout = html.Div(children=[
    html.H1(children='Bookseller Ningbo - Dashboard'),

    dcc.Graph(
    id='testGraph',
    figure={
    'data': [
                {'x': mergeFrame['date'], 'y': mergeFrame['invTotal'].values, 'type':'bar', 'name': 'Utilties and other Expenses'},
                {'x': mergeFrame['date'], 'y': mergeFrame['bookOrder_total'].values, 'type':'bar', 'name': 'Sales Revenue'},
                {'x': mergeFrame['date'], 'y': mergeFrame['sO_total'].values, 'type':'bar', 'name': 'Book Order Expense'}
            ],
            'layout': {
                'title': 'Revenue & Expenses'
} } ), ])
if __name__ == '__main__':
    app.run_server(debug=True)
