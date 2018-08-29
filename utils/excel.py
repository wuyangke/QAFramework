# Handle Excel file
import xlrd

class Excel:
    def read_row(self, path='data/testdata_api_advent.xlsx',sheet='testcase'):
        self = xlrd.open_workbook(path)
