import time
import unittest  # 单元测试模块
from utils.config import Config, DATA_PATH, REPORT_PATH  # 引入配置
from utils.logger import logger  # 引入日志模块
from utils.file_reader import ExcelReader  # 引入xls读取模块
from utils.HTMLTestRunner import HTMLTestRunner
from tomorrow import threads
from web.page.baidu_main_page import BaiDuMainPage
from web.page.baidu_result_page import BaiDuResultPage


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.driver.quit()  # 清理退出

    @threads(2)
    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()

def add_case(case_path='./', rule="test_*.py"):
    # 加载所有的测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


if __name__ == '__main__':
    # unittest.main()

    report = REPORT_PATH + '\\report.html'
    print(report)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='QA', description='测试报告')
        runner.run(add_case())
        #runner.run(TestBaiDu('test_search'))
        f.close()

    # e = Email(title='百度搜索测试报告',
    #           message='这是今天的测试报告，请查收！',
    #           receiver='...',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()
