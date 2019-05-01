import pandas as pd
import functions as f


order = f.readExcelFromFolder('excel', 'Order')

order = order.filter(['order_date', 'order_ID', 'order_location'], axis=1)
order['Weekday'] = order['order_date'].dt.dayofweek
order = order.groupby(['order_location', 'Weekday']).size()