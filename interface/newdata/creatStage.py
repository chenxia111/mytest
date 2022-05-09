import random
from common. Connectdb import DB


class creatStage():
    db = DB()

    def __init__(self,projectName):
        self.projectName = projectName

    def random_stage_name(self):
        """随机生成一个地块名"""
        print("---stageName---")
        while True:
            s1 = "期"
            number = random.randint(1, 10)
            stageName = str(number) + s1
            # 判断数据库中是否存在该用户名，
            res = self.db.find_count("SELECT * FROM de_p054_list_data WHERE stageName='{}' and projectName='{}'".format(stageName,self.projectName))
            if res == 0:
                return stageName




