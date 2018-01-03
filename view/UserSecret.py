#!/usr/bin/env python
#coding:utf-8

import  hashlib
def usersecret(message):
    data = hashlib.md5()
    data.update(message)
    result = data.hesdigest()
    return  result