#coding:utf-8

from bs4 import BeautifulSoup
# import urllib
# from urllib import parse
from ..config.bd_picture_con import baidu_pic,req_num
from .json_to_url import json_to_url
from .run_data_to_sql import run_data_sql
from .baidu_picture_api import db_pic_api
from .create_to_os import creat_mkdir
import re


def htm_abruption(htm,url):
    search = []
    htm =  BeautifulSoup(htm.content,"html.parser") #htm.content
    # print(htm)
    htndat = htm.find('div',{'class':'view-con'}).find_all("ul")

    for list_ui in range(len(htndat)):
        li_data = htndat[list_ui].find_all('li',{})
        for list_li in range(len(li_data)):
            baidu_pic["tag"] = li_data[list_li].a["tag2"]
            baidu_pic["tag3"] = li_data[list_li].a["label"]
            n_data = [baidu_pic["tag"], baidu_pic["tag3"]]
            baidu_pic["pn"] = 0
            path_pic = "\\" + baidu_pic["tag"] +"\\"
            if baidu_pic["tag3"]:
                path_pic = path_pic  + baidu_pic["tag3"] +"\\"
            if n_data not in search:
                get_pic = True
                search.append(n_data)
                creat_mkdir("..\data"+path_pic)
                while get_pic:
                    htmlurl = json_to_url(baidu_pic)
                    get_pic = db_pic_api(htmlurl,url,path_pic)
                    baidu_pic["pn"] += req_num
                    print(baidu_pic["pn"])
    # print(htndat[0])
    d = htndat[0].find_all('li',{})
    print(d[1].a["tag2"])
