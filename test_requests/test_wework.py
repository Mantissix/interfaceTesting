import requests

from test_requests import home


class Testwework:
    # 部门创建
    def test_creat_dep(self, gettoken):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={gettoken}"
        body = {
            "name": "成都研发中心",
            "name_en": "RDCD",
            "parentid": 1,
            "order": 2,
            "id": 3
        }
        r = requests.request("POST", url, json=body)
        assert r.json()['errcode'] == 0

        depart_info = self.test_depsearch(gettoken)
        assert depart_info['department'][2]['name'] == "成都研发中心"

    #
    def test_depsearch(self, gettoken):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={gettoken}"

        r = requests.request("GET", url)
        assert r.json()['errcode'] == 0
        return r.json()

    #
    def test_depdelete(self, gettoken):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={gettoken}&id=3"

        r = requests.request("get", url)
        assert r.json()['errmsg'] == 'deleted'

        depart_info = self.test_depsearch(gettoken)
        assert len(depart_info['department']) == 2

    #
    def test_depupdate(self, gettoken):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={gettoken}"
        body = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 2,
            "id": 2
        }
        r = requests.request("POST", url, json=body)

        depart_info = self.test_depsearch(gettoken)
        assert depart_info['department'][1]['name'] == "广州研发中心"
