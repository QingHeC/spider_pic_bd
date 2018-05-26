#coding:utf-8

import sqlite3
# import pymysql


class create_sql_table():
    def __init__(self):
        self.sqldb = sqlite3.connect("../lib/url_table.db")
        self.cursor_sql = self.sqldb.cursor()
    def create_sql(self,sql_str):
        data = self.cursor_sql.execute(sql_str)
        return data
    def insert_sql(self,sqlstr):
        try:
            self.cursor_sql.execute(sqlstr)
            data = self.sqldb.commit()
        # except:
        except sqlite3.Error as a:
            # data = self.sqldb.rollback()
            # data = self.sqldb.row_factory()
            data = a.args
            # print(a)
        return data

    def select_sql(self,sqlstr):
        try:
            resdata = self.cursor_sql.execute(sqlstr)
            data = resdata.fetchall()
        # except sqlite3.Error as a:
        except:
            data = self.sqldb.rollback()
            # data = a.args
            # data = self.sqldb.row_factory()

        return data

    # def __del__(self):
    #     self.sqldb.close()


if __name__ == "__main__":

#---------------------------------------
    sq = create_sql_table()



#url_name存放进行访问的url
    sqls1 = '''create table dotwn_url(
                url_id INTEGER primary key  AUTOINCREMENT,
                url_name varchar(255) not null,
                url_source_url varchar(255),
                url_down Boolean DEFAULT 0  
            ) '''
    sq.create_sql(sqls1)

    insta_sql = '''
                insert  into dotwn_url(url_name,url_cookies) VALUES ("http://www.baidu.com","cokie")
                '''
    # sq.insert_sql(insta_sql)

    select_sql ='''
                select * from dotwn_url where url_name = 'http://image.baidu.com/channel/wallpaper';
                '''
    # retsqp = sq.select_sql(select_sql)
    # print(retsqp)
    # for lis in retsqp:
    #     print(lis)

#----------------------------------------------
#路径 名字 链接 对应cook 是否下载
    sql_url_pict = '''
                create table pict_posit(
                      pict_id INTEGER PRIMARY key AUTOINCREMENT,
                      pict_name char(60),
                      pict_links VARCHAR(255),
                      pict_path VARCHAR(225),
                      pict_desc VARCHAR(255),
                      pict_source VARCHAR(255),
                      pict_down Boolean DEFAULT 0
                )
                '''
    sq.create_sql(sql_url_pict)