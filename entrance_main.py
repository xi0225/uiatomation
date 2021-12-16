import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append(os.getcwd())

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

now = time.strftime("%Y-%m-%d-%H-%M-%S")
# suite = unittest.TestSuite()
# suite.addTest(TestLogin("test_search"))
# suite.addTest(TestLogin("test_search1"))
# suite.addTest(TestLogin("test_search2"))
CaseDir = BASE_DIR+'\\testcase\\'
discover = unittest.defaultTestLoader.discover(start_dir=CaseDir, pattern="test_baiduSearch.py")

path = BASE_DIR + '\\report\\'+ now + "result.html"
fp = open(path, 'wb')

runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试查询功能")
runner.run(discover)
fp.close()