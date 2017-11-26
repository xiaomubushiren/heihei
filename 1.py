# -*- coding:utf-8 -*-
import unittest
import json
import requests
import htmltestrunner
#from datetime import datetime
import time

class ApiTest(unittest.TestCase):
    #创建活动url
    def setUp(self):
        self.url = "http://47.92.88.246:8001/api/add_activity/"
        self.search_url = "http://47.92.88.246:8001/api/search_activity/"
        self.del_url = "http://47.92.88.246:8001/api/del_activity/"
        #self.now_time = datetime.now().strftime('%Y%m%d%H%M%S')
        self.now_time = int(round(time.time())*1000)
        print self.now_time
        #self.request_data = {"activity_name": '三国杀2', "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
        #            "start_time": "20171902", "end_time": "2018982"}
    #添加项目
    # def test_Add_Activity_01(self):
    #     response_obj = requests.post(self.url,json.dumps(self.request_data))
    #     res = json.loads(response_obj.text)
    #     self.assertEqual(res['status'],-2)

    # def test_Add_Activity_02(self):
    #     self.request_data["activity_name"] = "三国杀" + str(self.now_time)
    #     response_obj = requests.post(self.url, json.dumps(self.request_data))
    #     res = json.loads(response_obj.text)
    #     self.assertEqual(res['status'],0)

    #活动名称不能超过20字
    # def test_Name_longth(self):
    #     self.request_data = {"activity_name": '三国杀2', "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
    #                          "start_time": "20171902", "end_time": "2018982"}

    #查询活动
    # def test_search_activity(self):
    #     self.request_data = {"activity_name": '三国杀2'}
    #     result = requests.post(self.search_url,json.dumps(self.request_data))
    #     res = json.loads(result)
    #     self.assertEqual(res['status'],0)

    #删除活动
    def test_delent_activity(self):
        #创建活动
        status = self.add_activity("京东12345678")
        self.assertEqual(status,0)
        #查询活动
        self.data = self.search_activity("京东12345678")
        #查询Id
        id = self.data['id']
        #删除活动
        status = self.del_activity(id)
        #验证活动是否删除
        self.assertEqual(status,0)
    #添加活动
    def add_activity(self,activty_name):
        self.request_data = {"activity_name": '三国杀2', "activity_desc": "几个人周末一起玩", "activity_project": "篮球",
                             "start_time": "20171902", "end_time": "2018982"}
        self.request_data["activity_name"] = activty_name
        response_obj = requests.post(self.url, json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['status']

    #查询红的
    def search_activity(self,activty_name):
        self.request_data = {"activity_name": activty_name}
        response_obj = requests.post(self.search_url, json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['data'][0]

    #删除
    def del_activity(self,id):
        self.request_data = {"id": id}
        response_obj = requests.post(self.del_url, json.dumps(self.request_data))
        res = json.loads(response_obj.text)
        return res['status']

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(ApiTest("test_delent_activity"))
    filename = r'/usr/local/test/wang.html'
    print filename
    fp = open(filename,'wb+')
    runner = htmltestrunner.HTMLTestRunner(
        stream=fp,
        title='testresult',
        description='testreport'
    )
    runner.run(suite)
    fp.close()
