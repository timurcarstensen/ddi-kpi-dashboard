import pandas as pd
import functions as f

order = f.readExcelFromFolder('excel', 'Order')

customer = f.readExcelFromFolder('excel', 'Customer')
customer = customer.rename(columns={'cus_ID':'customerID'}, inplace=False)

order = order.rename(columns={'order_customerID':'customerID'}, inplace=False)
order = order.merge(customer, on='customerID', how='outer')


orderM = len(order.loc[(order.cus_gender == 'M')])
orderF = len(order.loc[(order.cus_gender == 'F')])
orderNaN = len(order) - (orderM + orderF)



