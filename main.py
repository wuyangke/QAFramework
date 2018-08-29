import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner


# load cases from path with rule
def load_cases(path='./test', rule="test_api_*.py"):
    discover = unittest.defaultTestLoader.discover(path, pattern=rule, top_level_dir=None)
    return discover


if __name__ == '__main__':

    report = REPORT_PATH + '\\report.html'
    print(report)
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='QA', description='测试报告')
        runner.run(load_cases())
        f.close()
