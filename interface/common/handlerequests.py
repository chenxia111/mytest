import requests


class SendRequest(object):
    """cookie+session鉴权的请求类封装"""

    def __init__(self):
        self.session = requests.session()

    def send_requests(self, url, method, headers=None, params=None, data=None, json=None, files=None):
        method = method.lower()
        if method == "get":
            response = self.session.get(url= url, params=params, headers= headers)
        elif method == "post":
            response = self.session.post(url= url,json= json, data= data, headers = headers, files = files)
        elif method == "patch":
            response = self.session.post(url= url,json= json, data= data, headers = headers, files = files)

        return response