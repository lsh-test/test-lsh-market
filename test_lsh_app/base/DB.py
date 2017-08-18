#-*- coding: utf-8 -*-
import ConfigParser
import os

import MySQLdb

class DB:
    #商城库
    def  getMarketConnection(self):
        cf = ConfigParser.ConfigParser()
        cf.read(os.path.dirname(os.getcwd()) + "/conf/app_config.ini")
        HOST = cf.get("db_market_conf", "db_host")
        PORT = cf.get("db_market_conf", "db_port")
        USER = cf.get("db_market_conf", "db_user")
        #PW = cf.get("db_market_conf","db_password")
        DB = cf.get("db_market_conf", "db_name")
        dbConnect = MySQLdb.Connect(host=HOST, port=int(PORT), user=USER, db=DB,charset="utf8")
        return dbConnect

    def marketQuery(self,sql):
        mysql = DB()
        mysqldb = mysql.getMarketConnection()
        cursor = mysqldb.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            #print data
        except:
            print "Error: unable to fecth data"
        mysqldb.close()
        return data

    def marketUpdate(self, sql):
        mysql = DB()
        mysqldb = mysql.getMarketConnection()
        cursor = mysqldb.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            mysqldb.commit()
        except:
            mysqldb.rollback()
        mysqldb.close()

    #销售库
    def  getSalesConnection(self):
        cf = ConfigParser.ConfigParser()
        cf.read(os.path.dirname(os.getcwd()) + "/conf/app_config.ini")
        HOST = cf.get("db_sales_conf", "db_host")
        PORT = cf.get("db_sales_conf", "db_port")
        USER = cf.get("db_sales_conf", "db_user")
        #PW = cf.get("db_madb_sales_confrket_conf","db_password")
        DB = cf.get("db_sales_conf", "db_name")
        dbConnect = MySQLdb.Connect(host=HOST, port=int(PORT), user=USER, db=DB,charset="utf8")
        return dbConnect

    def salesQuery(self,sql):
        mysql = DB()
        mysqldb = mysql.getSalesConnection()
        cursor = mysqldb.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
        except:
            print "Error: unable to fecth data"
        mysqldb.close()
        return data

    def salesUpdate(self, sql):
        mysql = DB()
        mysqldb = mysql.getSalesConnection()
        cursor = mysqldb.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            mysqldb.commit()
        except:
            mysqldb.rollback()
        mysqldb.close()



#a = DB()
#a.salesQuery("select invite_code from invite_code where uid = 0 and zone_id = 1001 limit 1")

