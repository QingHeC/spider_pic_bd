#coding:utf-8

import requests
import urllib
from zuoye.config.bd_picture_con import baidu_pic
url = "http://image.baidu.com/channel/wallpaper#%E9%A3%8E%E6%99%AF&%E5%85%A8%E9%83%A8&8&0"
head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/57.0",
    "Host":"image.baidu.com"
}
#http://image.baidu.com/data/imgs?pn=0&rn=24&col=壁纸&tag=风景&tag3=全部&width=1366&height=768&ic=0&ie=utf8&oe=utf-8&image_id=&fr=channel&p=channel&from=1&app=img.browse.channel.wallpaper&t=0.4064753878641626
#http://image.baidu.com/data/imgs?pn=24&rn=24&col=壁纸&tag=风景&tag3=全部&width=1366&height=768&ic=0&ie=utf8&oe=utf-8&image_id=&fr=channel&p=channel&from=1&app=img.browse.channel.wallpaper&t=0.13608138901670042
#http://image.baidu.com/data/imgs?pn=0&rn=18&col=壁纸&tag=全部&tag3=&width=1366&height=768&ic=0&ie=utf8&oe=utf-8&image_id=&fr=channel&p=channel&from=1&app=img.browse.channel.wallpaper&t=0.3203739046964118
#http://image.baidu.com/data/imginfo?fr=channel&tag1=编辑推荐&tag2=全部&column=壁纸&tag=全部&ie=utf-8&oe=utf-8&word=1&t=1523698979418


# htm = requests.get(url)

# print(htm.content.decode())


# st = str(baidu_pic)
# st = st.replace(":","=")
# st = st.replace(",","&")
# st = "".join(st)
st =urllib.parse.urlencode(baidu_pic)
print(st)