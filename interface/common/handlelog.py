import logging
from common.handleconfig import conf
from common.handelpath import LOGDIR
import os

class HandleLog(object):

    @staticmethod
    def creat_logger():
        # 创建收集器，设置收集器的等级
        mylog = logging.getLogger(conf.get("log", "name"))
        mylog.setLevel(conf.get("log", "level"))

        # 创建输出到控制台的渠道，设置等级
        sh = logging.StreamHandler()
        sh.setLevel(conf.get("log", "sh_level"))
        mylog.addHandler(sh)

        # 创建输出到文件的渠道，设置等级
        fh = logging.FileHandler(os.path.join(LOGDIR, "log.log"), "a", encoding="utf8")
        fh.setLevel(conf.get("log", "fh_level"))
        mylog.addHandler(fh)

        # 设置日志输出格式
        formater = '%(asctime)s - [%(filename)s--->line:%(lineno)d] - %(levelname)s:%(message)s'
        fm = logging.Formatter(formater)
        # 将输出格式和输出渠道绑定
        sh.setFormatter(fm)
        fh.setFormatter(fm)

        return mylog

log = HandleLog.creat_logger()
log.info("python66666666")