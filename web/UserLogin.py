#!/usr/bin/env python
#coding:utf-8

from flask import  Flask,render_template,request,redirect,Response
from LogDisSys.Mysqlvilew.MysqlClass import UserLogin
from LogDisSys.view.LogSeach import LogGet
from LogDisSys.LogModule import  LogRecord
app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])
def userlogin():
    if request.method == "GET":
        return  render_template("login_design.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        count = UserLogin.select().where(UserLogin.username == username and UserLogin.password == password)
        if count:
            return  redirect("/index")
        else:
            return render_template("login_design.html")

@app.route("/register",methods=["GET","POST"])
def userregister():
    if request.method == "GET":
        return render_template("register.html")


@app.route("/index",methods=["GET","POST"])
def Index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/search",methods=["POST"])
def Search():
    startdate =  request.form.get("startdate")
    enddate =  request.form.get("enddate")
    keyvalue =  request.form.get("keyvalue")
    service =  request.form.get("service")
    result = LogGet(startdate=startdate,enddate=enddate,keyvalue=keyvalue,service=service)
    # print result
    return Response(result)
if __name__ == "__main__":
    logger = LogRecord.logger
    logger.warning("tiaoshi")
    app.run()
