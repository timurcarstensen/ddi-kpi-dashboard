import pandas as pd
import functions as f


session = f.readExcelFromFolder('excel', 'UserSession')

session[['userSession_endTime', 'userSession_startTime']] = session[['userSession_endTime', 'userSession_startTime']].astype('datetime64')
session['sessionTime'] = session['userSession_endTime'] - session['userSession_startTime']
session['Weekday'] = session['userSession_startTime'].dt.dayofweek
session = session.groupby('Weekday').size()
session = session.to_frame()






