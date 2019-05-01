import pandas_access as mdb
import pandas as pd
import functions as f

file = "bookseller_ningbo.mdb"

tableNames = list()

for i in mdb.list_tables(file):
    print(i)
    tableNames.append(i)

for i in tableNames:
    try:
        df = mdb.read_table(file, i)
        f.toExcel(i, df)
    except:
        print(i + " read error")
        