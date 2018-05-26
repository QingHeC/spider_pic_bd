#coding:utf-8

import urllib


def json_to_url(json_data):
    url_para = urllib.parse.urlencode(json_data)
    return url_para