import random
from common. Connectdb import DB

class creatProject():
    db = DB()

    @classmethod
    def random_project_name(cls):
        """随机生成一个地块名"""
        print("---projectName---")
        while True:
            s1 = "SHXM"
            number =random.randint(1, 999999)
            projectName = s1 + str(number)
            # 判断数据库中是否存在该用户名，
            res = cls.db.find_count("SELECT * FROM de_p051_list_data WHERE projectName='{}'".format(projectName))
            if res == 0:
                return projectName

