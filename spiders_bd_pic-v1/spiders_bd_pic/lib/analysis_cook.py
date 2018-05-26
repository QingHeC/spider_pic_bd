#coding:utf-8


def data_cook_json(data):
    jar=''
    cont = 0
    for key , value in data.items():
        ja =""
        cont+=1
        ja= key+'='+value
        jar +=ja
        if cont < len(data.items()):
            jar +=';'
    # print(jar)
    return jar
