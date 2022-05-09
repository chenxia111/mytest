"""
配置文件类的封装

封装的目的：使用更简单


封装的需求：

1、简化创建配置文件解析器对象，加载配置文件的流程（需要封装），提示（重写init方法）

2、读取数据（不进行封装，使用原来的方法），通过继承父类即可

3、简化写入数据的操作（需要封装），提示：自定义一个write_data方法。

"""
from configparser import ConfigParser
from common.handelpath import CONFDIR
import os

class HandleConfig(ConfigParser):
    """封装的读取配置文件类"""
    def __init__(self, file_name, encoding='utf-8'):
        """
        初始化
        file_name:配置文件名
        encoding:编码格式
        """
        super().__init__()
        self.file_name = file_name
        self.encoding = encoding
        self.read(file_name, encoding=encoding)

    def write_data(self, section, option, value):
        """

        :param section: 配置块
        :param option:配置属性
        :param value:对应的配置属性值
        """
        self.set(section, option, value)
        self.write(open(self.file_name, 'w', encoding=self.encoding))

conf = HandleConfig(os.path.join(CONFDIR, "config.ini"))