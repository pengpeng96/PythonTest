# -*- coding：utf-8 -*-
import unittest
class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.name = '小D课堂'
        self.age = 23
    def tearDown(self):
        print('测试结束')
# 用例名称
    def test_name(self):
        # 判断名字是否相同
        self.assertEqual(self.name,'小D课堂',msg = '名字不对')
# 用例名称
    def test_age(self):
        # 判断年龄是否一致
        self.assertEqual(self.age,23,msg=' ')
# 用例名称
    def test_isupper(self):
        # 判断括号里面的内容是否为错，若是则返回点(.),若不是，则返回msg
        self.assertFalse('xdclass'.upper(), msg='不是大写')
    # 调用TestSuite控制用例顺序
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserTestCase("test_age"))
    suite.addTest(UserTestCase("test_isupper"))
    suite.addTest(UserTestCase("test_age"))

    # TextTestRunner() 文本测试用例运行器,参数verbosity生成报告
    runner = unittest.TextTestRunner(verbosity=1)

    #run()方法是运行测试套件的测试用例，入参为suite测试套件
    runner.run(suite)