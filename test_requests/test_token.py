import requests


class Testtoken:

    def test_gettoken(self):
        # 获取access_token
        # 定义凭证
        corp_ID = "ww1c8de7ae916bc476"
        corp_secret = "a90CvcQM7sIH3SOOUxeDRF3hIFJhpyXpT_HM2zZPFsY"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corp_ID,
            "corpsecret": corp_secret
        }

        # 发出get请求
        r = requests.get(url, params)

        # 设置断言，验证测试结果
        assert r.status_code == 200
        assert r.json()['errmsg'] == 'ok'

        # 查看响应信息
        print(r.json())

    # def test_gettoken2(self):
    #     corp_ID = "ww1c8de7ae916bc476"
    #     corp_secret = "a90CvcQM7sIH3SOOUxeDRF3hIFJhpyXpT_HM2zZPFsY"
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_ID}&corpsecret={corp_secret}"
    #
    #     r = requests.request("GET", url)
    #     print(r.json())

    def test_getdepartment(self):
        access_token = ""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={access_token}&id=1"

        r = requests.request("POST", url)
        print(r.json())
