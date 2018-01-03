#!/usr/bin/env python
#coding:utf-8

import peewee
import os
import ConfigParser
import  time
config = ConfigParser.ConfigParser()
configfile = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.sep+"Configs"+os.sep+"Baseconfig.conf"
config.read(configfile)

class MysqlConn:
    def __init__(self,host,user,passwd,port,database,charset):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__port = port
        self.__database = database
        self.__charset = charset

    def initconn(self):
        conn = peewee.MySQLDatabase(
            host = self.__host,
            user =  self.__user,
            passwd = self.__passwd,
            port = self.__port,
            database = self.__database,
            charset = self.__charset
        )
        return  conn
mysqlinit = MysqlConn(config.get("test","host"),config.get("test","user"),config.get("test","passwd"),
            int(config.get("test","port")),config.get("test","database"),config.get("test","charset")).initconn()

class Servermatchip(peewee.Model):
    id = peewee.PrimaryKeyField()
    servername = peewee.CharField(max_length=50)
    serverIP = peewee.CharField(50)
    logpath = peewee.CharField(50)
    logname = peewee.CharField(50)
    create_date = peewee.DateTimeField()
    update_date = peewee.DateTimeField()
    class Meta:
        database = mysqlinit

class UserLogin(peewee.Model):
    id = peewee.PrimaryKeyField()
    username = peewee.CharField(max_length=30)
    password = peewee.CharField(max_length=50)
    create_date = peewee.DateTimeField()
    update_date = peewee.DateTimeField()
    class Meta:
        database = mysqlinit

if __name__ == "__main__":
    #Servermatchip.create_table()
    # Servermatchip.insert(servername="zabbix-proxy",serverIP="10.36.3.74",logpath="/tmp",logname="log.log",
    #                              create_date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),
    #                              update_date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())).execute()
    UserLogin.create_table()