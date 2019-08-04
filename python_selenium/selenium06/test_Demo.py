# -*- coding：utf-8 -*-
import unittest


class UserTestCase(unittest.TestCase):


    def tearDown(self):
        print("===tearDown===")

    def setUp(self):
        print("===setUp===")
        self.name = "小D课堂"
        self.age = 23

    def test_name(self):
        print("调用test_name")
        # 断言是否相同
        self.assertEqual(self.name,"小D课堂", msg= "名字不对")

    def test_isupper(self):
        print("调用test_isupper")

        # 断言是否为True,msg是断言错误的提示信息
        self.assertFalse("xdclass".isupper(), msg= "不是大写")

    def test_age(self):
        print("调用test_age")
        self.assertEqual(self.age,23)


if __name__  == '__main__':
    unittest.main()