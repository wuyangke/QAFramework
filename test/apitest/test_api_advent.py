import unittest
from utils.config import Config, DATA_PATH
from utils.file_reader import ExcelReader
import urllib3
import requests
import datetime
import pandas as pd
pd.core.common.is_list_like = pd.core.dtypes.inference.is_list_like
import pandas_datareader.data as web

session = requests.session()


class TestAdvent(unittest.TestCase):

    def setUp(self):
        urllib3.disable_warnings()

    def tearDown(self):
        session.close()

    def test_api_experiences(self):
        tds = ExcelReader(DATA_PATH + '/advent.xlsx', 'GET').data
        for td in tds:
            response = session.request('GET', td['url'].replace('{env}', Config().config.get('env')), verify=False)
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(response.elapsed, datetime.timedelta(seconds=10))

    def test_api_stock(self):
        start = datetime.datetime(2018, 8, 26)  # 获取数据的时间段-起始时间
        end = datetime.date.today()  # 获取数据的时间段-结束时间
        stock = web.DataReader('TSLA', 'robinhood', start, end)
        print(stock.head(5))
        print(stock.tail(5))


if __name__ == '__main__':
    unittest.main()
