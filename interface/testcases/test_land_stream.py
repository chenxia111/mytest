import pytest
import allure
import os
import jsonpath
import time
from common.readexcel import ReadExcel
from common.handelpath import DATADIR
from common.handleconfig import conf
from common.handlerequests import SendRequest
from common.handle_data import CaseDate,replace_data
from common.handlelog import log
from common. Connectdb import DB
from newdata.creatLand import creatLand


case_file = os.path.join(DATADIR,"api_cases_excel.xlsx")

current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
CaseDate.currentTime = current_time


class  TestReviewLand():
    excel = ReadExcel(case_file, "Land")
    cases = excel.read_data()
    request = SendRequest()
    db =DB()

    @allure.story("地块流程测试")
    @pytest.mark.parametrize('case',cases)
    def test_land_stream(self, case):
        #动态获取标题
        allure.dynamic.title(case['title'])
        allure.dynamic.severity(case['severity_level'])
        # json中属性为空的情况
        global null
        null = ''

        # 第一步：准备用例数据
        url = conf.get("env","url") + replace_data(case["url"])
        method =  case ["method"]
        headers = eval(conf.get("env", "headers"))


        # 判断是否是添加地块的用例，如果是则获取地块名称
        if case["interface"] == "create":
            # 随机生成地块名称
            CaseDate.landName = creatLand.random_land_name()


        data = eval(replace_data(case["data"]))

        # 判断是否是登录接口，不是登录接口需要添加Authorization
        if case["interface"] != "logintzwh" and case["interface"] != "logintzsp":
            # 投资维护登录主数据系统，获取Authorization
            headers["Authorization"] = getattr(CaseDate, "Authorization")

        # 获取预期值
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 第二步： 发送请求，获取结果
        print("请求参数：", data)
        response = self.request.send_requests(url=url, method=method, json=data, headers=headers)
        res = response.json()
        print("预期结果", expected)
        print("实际结果", res)
        # 发送请求后，判断是否是登陆接口
        if case["interface"].lower() == "logintzwh" or case["interface"] == "logintzsp":
            # 提取Authorization保存为类属性
            Authorization = jsonpath.jsonpath(res, "$..data")[0]
            # 将提取到的data设为CaseDate类属性
            CaseDate.Authorization = Authorization

        # 判断是否是添加地块的用例，如果是的则获取地块id
        if case["interface"] == "create":
            # 从CaseDate类中获取landName
            landName = getattr(CaseDate, "landName")
            # 获取地块id
            sql = "select id from de_r009_list_data where parcelName='{}'".format(landName)
            print("id的值：" + self.db.find_one(sql)["id"])
            print("打印sql：" + sql)
            CaseDate.id = self.db.find_one(sql)["id"]

        if case["interface"] == "review":
            # 地块发起审核后，获取process_id
            id = getattr(CaseDate,"id")
            sql = "SELECT process_id FROM de_r009_data_review_proc where data_id = '{}'".format(id)
            print("打印sql：" + sql)
            CaseDate.process_id = self.db.find_one(sql)["process_id"]

        if case["interface"] == "getTaskId":
            # 获取流程getTaskId
            taskId = jsonpath.jsonpath(res, "$..taskId")[0]
            # 将提取到的data设为CaseDate类属性
            CaseDate.taskId = taskId


        # 第三步：断言（比对预期结果和实际结果）
        try:
            pytest.assume(expected["code"] == res["code"])

        except AssertionError as e:
            print("预期结果：", expected)
            print("实际结果：", res)
            self.excel.write_data(row=row, column=8, value="未通过")
            allure.dynamic.description(case['result'])
            log.error("用例{}执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            allure.dynamic.description(case['result'])
            log.info("用例{}执行通过".format(case["title"]))
            log.info("实际结果：{}".format(res))

