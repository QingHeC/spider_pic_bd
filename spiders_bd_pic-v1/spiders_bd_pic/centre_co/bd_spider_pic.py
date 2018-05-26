#coding:utf-8

import requests
from spiders_bd_pic.config.bd_picture_con import url,url_picture_api
from spiders_bd_pic.lib.htm_abruption import htm_abruption
from spiders_bd_pic.lib.htm_spon_cooki import html_storage

class C_sipder():
    def __init__(self):
        self.url = url
        self.html_storage  = html_storage()
        #self.htm.content
    def abru_data(self):
        # self.htm,cookie = self.html_storage.html_url_cookie(self.url)
        self.htm,req_url = self.html_storage.html_url_cookie(self.url)
        # self.htm = requests.get(url=url)
        htm_abruption(self.htm,req_url)



if __name__ == "__main__":
    htm = C_sipder()
    htm.abru_data()