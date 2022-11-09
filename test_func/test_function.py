# -*- coding: utf-8 -*-
import json
import os
import unittest
import requests
from importlib import import_module
import inspect

from BeautifulReport import BeautifulReport
from unittestreport import TestRunner


class TestDivision(unittest.TestCase):
    # 初始化并赋值
    def setUp(self):
        if os.path.exists("json_data.json"):
            # 获取参数
            with open("json_data.json", "r") as f:
                data_list = json.loads(json.dumps(f.read()))
            self.data_list = json.loads(data_list)
        # 验证格式
        try:
            for key, info in self.data_list.items():
                necessary = info.get("necessary")
                expected_value = info.get("expected_value")
                if not all([necessary, expected_value]):
                    raise ValueError("第{}个字典参数错误,necessary和expected_value字段不可为空！！".format(key))
                if not all([necessary.get("path"), necessary.get("function")]):
                    raise ValueError("第{}个字典参数错误,necessary中path和function是必填字段！！".format(key))
                if not expected_value.keys():
                    raise ValueError(" 第{}个字典参数错误,expected_value中expected必须填一个！！".format(key))
        except Exception as e:
            print(e)
            return False
        # 导入方法
        for data in self.data_list.values():
            function = data.get("necessary").get("function")
            path = data.get("necessary").get("path")
            if function and path:
                print("{}.{}".format(path, function))
                self.func = getattr(import_module(path), function)
        return True

    def test_func_true(self):
        # 判断是否有错
        if not self.setUp():
            return
        # 获取方法需要传的参数 并且将文件中的参数格式化加入到方法中
        for key, data in self.data_list.items():
            necessary = data.get("necessary")
            expected = data.get("expected_value").get("expected")
            try:
                data_dict = dict()
                # 获取方法传的参数
                for i in inspect.getfullargspec(self.func).args:
                    if i in data.get("params").keys():
                        temp_dict = dict()
                        temp_dict[i] = data.get("params").get(i)
                        data_dict.update(temp_dict)
                func_test = self.func(**data_dict)
                self.assertEqual(func_test, expected)
            except Exception as e:
                print(
                    "\n测试数据：{}\n测试函数：{}\n测试结果：异常\n测试详情：\n返回值:{}，期待值：{}\n详情:\n{} \n\n".format(str(key), str(necessary.get("function")),
                                                                                    func_test, expected,
                                                                                    str(e)))
                continue
            print(
                "\n测试数据：{}\n测试函数：{}\n测试结果：正常\n测试详情：\n返回值:{}，期待值：{}\n详情:\n{} \n\n".format(str(key),
                                                                                         str(necessary.get("function")),
                                                                                         func_test, expected,
                                                                                         func_test))

if __name__ == "__main__":
    load = True
    while (load):
        # 测试用例保存的目录
        unittest.main()
        input_text = input("请输入q退出")
        if input_text == "q":
            load = False