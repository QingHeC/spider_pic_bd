#coding:utf-8

from ..config.bd_picture_con import datapath,headers
# from ..lib.htm_spon_cooki import html_url_cookie
import requests

def down_pic(pic_link,pic_path):
    #data[0]:url
    print(headers)
    path = datapath+pic_path
    print("下载文件： %s" %pic_link)
    req = requests.get(pic_link, headers=headers)
    print(req.status_code)
    print(path)
    with open(path,'wb') as file:
        # for dat in req.content:
        file.write(req.content)
        # file.close()

