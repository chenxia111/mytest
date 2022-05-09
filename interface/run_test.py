import pytest

if __name__=="__main__":
    pytest.main(["-v", "-s", ".","--alluredir=allure_report/","--clean-alluredir"])