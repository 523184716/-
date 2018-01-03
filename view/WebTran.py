#!/usr/bin/env python
#coding:utf-8

from Auth import SshConn
from LogDisSys.Mysqlvilew.MysqlClass import Servermatchip
from UserSecret import usersecret
from flask import  Flask,request,render_template,redirect
import  os


#print app


def webget():
    servicename = "zabbix-proxy"
    searchtime = ""
    keyword = "agent"
    count = Servermatchip.select(Servermatchip.serverIP,Servermatchip.logpath,Servermatchip.logname).where(Servermatchip.servername==servicename)
    if count:
        for i in count:
            print i.serverIP,i.logpath,i.logname
            logfile = i.logpath + "/"+i.logname
        command = "grep {} {}|tail -300".format(keyword,logfile)
        result=SshConn().execcommand(command)
        return  result
    else:
        print "sorry,此服务不存在"

#logprint = webget()
#print logprint

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8816,debug=True)