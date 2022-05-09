import os

# # 获取当前文件的绝对路径
# res = os.path.abspath(__file__)
# print(res)
# # 获取指定文件路径的父级目录路径
# res2 = os.path.dirname(res)
# print(res2)
#
# res3 = os.path.dirname(res2)
# print(res3)

# 项目目录路径
BASEIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEIR)

# 用例模块目录的路径
CASEDIR =os.path.join(BASEIR,"testcases")
print(CASEDIR)

# 用例数据目录的路径
DATADIR = os.path.join(BASEIR,"data")
print(DATADIR)

# 测试报告目录的路径
REPORTDIR =os.path.join(BASEIR, "reports")
print(REPORTDIR)

# 配置文件目录的路径
CONFDIR =os.path.join(BASEIR, "conf")
print(CONFDIR)

# 配置文件目录
LOGDIR = os.path.join(BASEIR, "logs")