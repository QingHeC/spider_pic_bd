#coding:utf-8

import urllib
import requests
import re ,json
from bs4 import BeautifulSoup
from ..config.bd_picture_con import url_picture_api,headers,datas_cook
from .htm_spon_cooki import html_storage
from .run_data_to_sql import run_data_sql
from ..centre_co.down_to_pic_ import down_pic

def db_pic_api(htmurl,sou_url,pic_path):
    """htmurl:链接，sou_url：来自url,pic_path:图片保存路径"""
    req_url = url_picture_api + htmurl
    print("url：%s" %req_url)
    #插入url链接树
    run_data_sql().run_data_insert_only_picapi(["dotwn_url",req_url,sou_url])
    # htm_api = requests.get(req_url)
    htm_api,sou_url = html_storage().html_url_cookie(req_url)

    htm_data_json = json.loads(htm_api.text)
    for data in htm_data_json["imgs"][:-1]:
        try:
            # print(htm_data_json["imgs"])
            # print(data)
            # if
            pict_name = data["imageUrl"].split("/")[-1]
            pict_links = data["imageUrl"]
            pict_path = pic_path
            pict_desc = data["desc"]
            pict_source = req_url
            run_data_sql().run_data_insert_only_pic_links(['pict_posit', pict_name, pict_links, pict_path, pict_desc, pict_source])
            # 存储路径 描述  pic地址  pic名字 源目录
            # datas = [data["desc"],data["imageUrl"],data["imageUrl"].split("/")[-1]]
            # print(datas)



        except:
            print(req_url)
            print("没有数据: ", end='')
            print(htm_data_json['tag'])
            return False

        if pict_desc:
            headers["Cookie"] = datas_cook[sou_url]
            print("1cookie")
            path_save = pict_path + pict_name
            down_pic(pict_links, path_save)
    return True





