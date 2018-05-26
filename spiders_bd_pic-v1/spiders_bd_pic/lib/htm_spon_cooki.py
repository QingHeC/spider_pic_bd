#coding:utf-8

from urllib import request
import requests
import http.cookiejar as cookies
from ..lib.run_data_to_sql import run_data_sql
from ..lib.create_sql import create_sql_table
import json,re
from ..config.bd_picture_con import header,headers,datas_cook
from .analysis_cook import data_cook_json




class html_storage():
    def __init__(self):
        self.runsql = run_data_sql()
    def html_url_cookie(self,url):
        """存储cookie"""

        data = self.runsql.run_data_sqlselect(["dotwn_url", "url_name",url])

        if data :
            data_hos = data[0][2]

            if data_hos != None:
                headers["Cookie"] = datas_cook[data_hos]

        req = requests.get(url,headers=headers)
        cookie = req.cookies
        data_jar_str = data_cook_json(cookie)
        datas_cook[url] = data_jar_str
        print("----datas_cook----")

        return  req,url


