#coding:utf-8

from ..lib.create_sql import create_sql_table

class run_data_sql(create_sql_table):
    def __init__(self):
        self.data_sql = create_sql_table()
    def run_data_insert_only_pic_links(self,data):
        cont = self.run_data_sqlselect([data[0],'pict_links',data[2]])
        sqlstr = ''
        if cont == ''or cont == [] or cont == None:
            sqlstr = """insert  into %s (pict_name,pict_links,pict_path,pict_desc,pict_source) VALUES ('%s','%s','%s','%s','%s');""" %(data[0],data[1],data[2],data[3],data[4],data[5])
        # print(sqlstr)
        if sqlstr:
            retdata = self.data_sql.insert_sql(sqlstr)
        # print("保存数据到SQL")
        # print(retdata)

    def from_sql_data(self):
        pass

    def run_data_insert_only_picapi(self, data):
        """url_name只允许有一个"""
        sqlstr = ''
        cont = self.run_data_sqlselect([data[0],'url_name',data[1]])
        # print("cont ; %s" %cont)
        if cont == ''or cont == [] or cont == None:
            # print("sql没有数据")
            sqlstr = """insert  into %s (url_name,url_source_url) VALUES ('%s','%s');""" % (data[0], data[1], data[2])
            # print(sqlstr)
        elif str(cont[0][1]) != str(data[1]):

            sqlstr = """select * from %s url_source_url=%s where url_id = %s """%(data[0],data[2],cont[0][0])
        else:
            pass

        if sqlstr:
            retdata = self.data_sql.insert_sql(sqlstr)
            # print("保存数据到SQL")
            # print(retdata)

    def run_data_sqlselect(self,data):
        # print(data)
        # print(type(data[0]))
        sqlstrt ="""select * from %s where %s = "%s";""" %(data[0],data[1],data[2])
        # print(sqlstrt)
        retdata = self.data_sql.select_sql(sqlstrt)
        return retdata

if __name__ == "__main__":
    asq = run_data_sql()
    url = 'http://image.baidu.com/channel/wallpaper'
    datastr = ["dotwn_url", "url_name", url]
    dat = asq.run_data_sqlselect(datastr)
    # print(dat)