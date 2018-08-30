# Handle Excel file with pandas
import pandas as pd
import os


class Excel:
    def __init__(self, file_name, sheet_name=0):
        with pd.ExcelFile(file_name) as xlsx:
            self.xlsx = xlsx
            self.df = pd.read_excel(xlsx, sheet_name)

    def get_sheet(self, sheet_name=0, header=0, index_col=None, usecols=None):
        return pd.read_excel(self.xlsx, sheet_name=sheet_name, header=header, index_col=index_col, usecols=usecols)


if __name__ == '__main__':
    root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    excel = Excel(root+'/data/project_a.xlsx')
    print(excel.get_sheet('Sheet1'))
    print(excel.get_sheet('Sheet1', header=0, index_col=0, usecols=[0, 1, 2, 5]))
