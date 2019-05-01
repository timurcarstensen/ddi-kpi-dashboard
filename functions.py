import pandas as pd


def toExcel(name: str, df): #saves dataframe to .xlsx file
    # import pandas as pd
    w = pd.ExcelWriter(name + '.xlsx')
    df.to_excel(w, 'Sheet1', index=False)
    w.save()

def readExcelFromFolder(folder: str, file: str):
    i = pd.read_excel(folder + "/" + file + ".xlsx")
    return i