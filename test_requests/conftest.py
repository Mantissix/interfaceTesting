import pytest
import requests


@pytest.fixture
def gettoken():
    corp_id = "ww1c8de7ae916bc476"
    corp_secret = "a90CvcQM7sIH3SOOUxeDRF3hIFJhpyXpT_HM2zZPFsY"
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    params = {
        "corpid": corp_id,
        "corpsecret": corp_secret
    }
    r = requests.get(url, params)

    token = r.json()['access_token']
    return token
