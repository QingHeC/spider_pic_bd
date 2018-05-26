#coding:utf-8
import os,time


url = "http://image.baidu.com/channel/wallpaper"
url_picture_api = "http://image.baidu.com/data/imgs?"
baidu_pic = {
    "pn":0,  # 访问变值 *p
    "rn":60, #加载图片数量默认60
    "col":"壁纸", #
    "tag":"风景",  #图片集合
    "tag3":"全部",  #图片描述类
    "width":"1366", #图片分辨率wid
    "height":"768", #图片分辨率hei
    "ic":"0",
    "ie":"utf8",
    "oe":"utf-8",
    "image_id":"",
    "fr":"channel",
    "p":"channel",
    "from":"1",
    "app":"img.browse.channel.wallpaper",
    #"t":"0.37916892797911095" #变值
}
req_num = 60

#datapath
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')

libpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'lib')
#objpath
objpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


header = (
    "User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Cookie":""
}


datas_cook = {}