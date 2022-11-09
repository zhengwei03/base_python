# -*- coding: utf-8 -*-
import json
import os
import unittest
from importlib import import_module

import requests
from django.core.paginator import Paginator


class TestApi:
    def __init__(self, data):
        self.data = data

    # get方法
    def send_get(self):
        # 获取url
        url = self.data.get("necessary").get('url') + "?"
        # 构造url
        for key, value in self.data.get("params").items():
            key = str(key)
            value = str(value)
            key += "="
            value = value + "&"
            url = url + key + value
        # 请求
        res = requests.get(url)
        # 获取期待值
        expected_value = self.data.get("expected_value")
        # 根据期望值返回
        for expect_key in expected_value.keys():
            if expect_key == "status":
                if res.status_code == 200:
                    # 请求成功
                    info = eval(res.content.decode("utf-8"))
                    res = {"data": info.get("data"), "message": info.get("message"), "status": info.get("status"), "status_code": res.status_code}
                    if not (info.get("message") or info.get("status")):
                        res = {"data": "List接口访问正确", "message": "List接口访问正确", "status": 200,
                               "status_code": res.status_code}
                    return res
                else:
                    # 请求失败
                    info = res.content.decode("utf-8")
                    res = {"data": info, "message": "状态异常", "status_code": res.status_code, "status": "error"}
                    return res
            elif expect_key == "status_code":
                # 状态码
                info = res.content.decode("utf-8")
                res = {"data": info, "message": "状态异常", "status_code": res.status_code, "status": "error"}
                return res
    # POST请求
    def send_post(self):
        # url获取
        url = self.data.get("necessary").get('url')
        # 参数获取
        res = requests.post(url, self.data.get("params"))
        # 期望值获取
        expected_value = self.data.get("expected_value")
        # 根据不同期望值返回不同数据
        for expect_key in expected_value.keys():
            if expect_key == "status":
                # 请求正常
                if res.status_code == 200:
                    info = eval(res.content.decode("utf-8"))
                    res = {"message": info.get("message"), "status": info.get("status"), "status_code": res.status_code, "data": info.get("data")}
                    return res
                else:
                    # 请求不正常
                    info = res.content.decode("utf-8")
                    res = {"message": "状态异常", "status_code": res.status_code, "status": "error", "data": info}
                    return res
            elif expect_key == "status_code":
                # 期望值为状态码
                info = res.content.decode("utf-8")
                res = {"message": "状态异常", "status_code": res.status_code, "status": "error", "data": info}
                return res
            else:
                return False



class TestDivision(unittest.TestCase):
    def setUp(self):
        # 判断文件是否存在
        if os.path.exists("json_data.json"):
            # 通过json_data.json来获取
            with open("json_data.json", "r") as f:
                data_dict = json.loads(json.dumps(f.read()))
            # 赋值
            self.data_dict = json.loads(data_dict)
        try:
            # 判断data的格式
            for key, info in self.data_dict.items():
                # 必要参数
                necessary = info.get("necessary")
                # 期望参数
                expected_value = info.get("expected_value")
                # 判断格式
                if not all([necessary, expected_value]):
                    raise ValueError("第{}个字典参数错误,necessary和expected_value字段不可为空！！".format(key))
                if not all([necessary.get("url"), necessary.get("method")]):
                    raise ValueError("第{}个字典参数错误,necessary中url和mothod是必填字段！！".format(key))
                if "status" in expected_value.keys() and "status_code" in expected_value.keys():
                    raise ValueError(" 第{}个字典参数错误,expected_value中status和status_code只能填一个！！".format(key))
                if not ("status" in expected_value.keys() or "status_code" in expected_value.keys()):
                    raise ValueError(" 第{}个字典参数错误,expected_value中status和status_code必须填一个！！".format(key))
        except Exception as e:
            print(e)
            return False
        return True

    def test_api(self):
        if not self.setUp():
            return
        # 遍历字典
        print("接口单元测试：\n")
        for key, data in self.data_dict.items():
            test = TestApi(data)
            # 必传值
            necessary = data.get("necessary")
            # get
            if necessary.get("method") == "get":
                get_info = test.send_get()
                try:
                    value_expect = ""
                    # 期望值
                    expected_value = data.get("expected_value")
                    # 判断期望值
                    for expect_key in expected_value.keys():
                        value_expect = expected_value.get(expect_key)
                        if expect_key == "status":
                            self.assertEqual(get_info.get("status"), value_expect, msg='not')
                        elif expect_key == "status_code":
                            self.assertEqual(get_info.get("status_code"), value_expect, msg='not')
                except Exception as e:
                    print("\n测试数据：{}\n测试接口：{}\n测试结果：异常\n测试详情： \n状态码:{}，期待状态码： {}\n 详情:\n {} \n\n".format(str(key), str(necessary.get("url")), get_info.get("status_code"), value_expect, get_info.get("data")))
                    continue
                print(
                    "\n测试数据：{}\n测试接口：{}\n测试结果：正常\n测试结果\n状态码:{}，期待状态码： {}\n 详情: {} \n\n".format(str(key), str(necessary.get("url")),
                                                                                    get_info.get("status"), value_expect,
                                                                                    get_info.get("data")))
            elif necessary.get("method") == "post":
                post_info = test.send_post()
                try:
                    value_expect = ""
                    expected_value = data.get("expected_value")
                    for expect_key in expected_value.keys():
                        value_expect = expected_value.get(expect_key)
                        if expect_key == "status":
                            self.assertEqual(post_info.get("status"), value_expect)
                        elif expect_key == "status_code":
                            self.assertEqual(post_info.get("status_code"), value_expect)
                except Exception as e:
                    # status = expected_value.get("status") if expected_value.get("status") else expected_value.get("status_code")
                    if post_info.get("data"):
                        print("\n测试数据：{}\n测试接口：{}\n测试结果：异常1\n测试详情:\n状态码:{}，期望状态码：{}\n详情:\n{} \n\n".format(str(key), str(necessary.get("url")), post_info.get("status_code"), value_expect, post_info.get("data")[:200]))
                    else:
                        print("\n测试数据：{}\n测试接口：{}\n测试结果：异常2\n测试详情:\n状态码:{}，期望状态码：{}\n详情:\n{} \n\n".format(str(key), str(
                            necessary.get("url")), post_info.get("status"), value_expect, post_info.get("message")))
                    continue
                print(
                    "\n测试数据：{}\n测试接口：{}\n测试结果：正常\n测试详情:\n 返回状态码:{}，期望状态码：{}\n详情:\n{} \n\n".format(str(key), str(necessary.get("url")),
                                                                                    post_info.get("status"), value_expect,
                                                                                    post_info.get("message")))


if __name__ == '__main__':
    unittest.main()




