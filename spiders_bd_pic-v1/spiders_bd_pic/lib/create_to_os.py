#coding:utf-8

import os

def creat_mkdir(path):
    print("path :%s" %path)
    try:
        if os.path.exists(path):
            pass
        else:
        #os.mkdir(path)
            os.makedirs(path)
        print("创建路径成功：%s"%path)
    except:
        print("创建路径失败成功：%s" % path)