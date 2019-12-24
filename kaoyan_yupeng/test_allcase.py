import unittest,time
from third_party_tools.HTMLTestRunner import HTMLTestRunner

discover=unittest.defaultTestLoader.discover('./case/',pattern='*testcase.py')
nowtime=time.strftime('%Y_%m_%d_%H_%M_%S')
report_name='./report/'+nowtime+'_report.html'
with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title='APP自动化测试用例执行结果',description='操作系统:Windows 7  python+selenium')
    runner.run(discover)