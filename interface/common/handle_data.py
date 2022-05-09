import re
from  common.handleconfig import conf


class CaseDate:
    """这个类专门用来保存，执行过程中提取出来给其他用例用的数据"""
    pass

def replace_data(s):
    r1 = r"#(.+?)#"
    while re.search(r1, s):
        res = re.search(r1, s)
        key = res.group(1)
        try:
            value = conf.get("test_data", key)
        except Exception:
            value = getattr(CaseDate,key)
        finally:
            s = re.sub(r1, value, s, 1)
    return s

if __name__ == "__main__":
    pass