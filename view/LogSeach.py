#!/usr/bin/env python
#coding:utf-8
from LogDisSys.Mysqlvilew.MysqlClass import Servermatchip
from Auth import  SshConn
from LogDisSys.LogModule import  LogRecord
def LogGet(**kwargs):
    startdate =  kwargs["startdate"]
    enddate = kwargs["enddate"]
    service = kwargs["service"]
    keyvalue = kwargs["keyvalue"]
    count = Servermatchip.select("serviceIP","logpath","logname").where(Servermatchip.servername == service).count()
    # print count
    if count:
        message = Servermatchip.select().where(Servermatchip.servername == service)
        for result  in message:
            # print result.serverIP,result.logpath,result.logname
            serviceaddr = result.serverIP
            logpath = result.logpath
            logname = result.logname
            command = "egrep {} {}/{}".format(keyvalue,logpath,logname)
            # print command
            result = SshConn().execcommand(command)
            # print result
            return  result
    else:
        return "请求的服务器不存在"

logger = LogRecord.logger
logger.warning("tiaoshi")