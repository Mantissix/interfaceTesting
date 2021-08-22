import requests


def get_request(url):
    requests.request("GET", url)
    return get_request(url)


def post_request(url, msg):
    requests.request("POST", url, json=msg)
    return post_request(url, msg)
