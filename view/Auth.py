#!/usr/bin/env python
#coding:utf-8
import ConfigParser
import os
from LogDisSys.LogModule import LogRecord
import  paramiko
# logger = LogRecord.logger
# logger.info("ceshi")

config = ConfigParser.ConfigParser()
configfile = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.sep+"Configs"+os.sep+"Baseconfig.conf"
config.read(configfile)

class SshConn:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.allow = self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__host = config.get("ssh","host")
        self.__port = int(config.get("ssh","port"))
        self.__username = config.get("ssh","username")
        self.__password = config.get("ssh","password")

    def sshinit(self):
        self.ssh.connect(hostname=self.__host,port=self.__port,username=self.__username,password=self.__password)

    def execcommand(self,command):
        self.sshinit()
        stdin,stdout,stdeor = self.ssh.exec_command(command)
        result = stdout.read()

        return  result

    def sshclose(self):
        self.ssh.close()



if __name__ == "__main__":
    command = "grep agent /tmp/log.log|tail -300"
    result = SshConn()
    logprint = result.execcommand(command)
    result.sshclose()
    print logprint