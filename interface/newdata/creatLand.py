import random
from common. Connectdb import DB

class creatLand():
    db = DB()

    @classmethod
    def random_land_name(cls):
        """随机生成一个地块名"""
        print("---landName---")
        while True:
            s1 = "SHDK"
            number =random.randint(1, 999999)
            landName = s1 + str(number)
            # 判断数据库中是否存在该用户名，
            res = cls.db.find_count("SELECT * FROM de_r009_list_data WHERE parcelName='{}'".format(landName))
            if res == 0:
                return landName



