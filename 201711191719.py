# -*- coding:utf-8 -*-
import requests
import unittest
import json
import time

class ApiTest(unittest.TestCase):
    #创建活动url
    def setUp(self):
        self.add_url = "http://47.92.88.246:8001/api/add_activity/"
        self.search_url = "http://47.92.88.246:8001/api/search_activity/"
        self.del_url = "http://47.92.88.246:8001/api/del_activity/"

        # 删除活动
    def test_del_activity(self):
        # 第一步创建一个活动
        status = self.add_activity("苏宁双十一6")
        self.assertEqual(status, 0)

        # 查询这个活动
        data = self.search_activity("苏宁双十一6")
        # 从返回结果中获取id
        id = data["id"]
        # 删除这个活动
        status = self.del_activity(id)
        # 验证是否删除成功
        self.assertEqual(status, 0)

        # 添加活动
    def add_activity(self, activity_name):
        self.request_data = {"activity_name": '三国杀2', "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
                             "start_time": "20171102", "end_time": "20180912"}
        self.request_data["activity_name"] = activity_name
        response_obj = requests.post(self.add_url, json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['status']

        # 查询活动

    def search_activity(self, name):
        self.requests_data = {"activity_name": name}
        response_obj = requests.post(self.search_url, json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['data'][0]

    # 删除活动
    def del_activity(self, id):
        self.request_data = {"id": id}
        response_obj = requests.post(self.del_url, json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['status']

if __name__ == "__main__":
    unittest.main()