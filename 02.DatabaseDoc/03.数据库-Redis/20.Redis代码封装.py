# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

import redis

class MyRedis(object):

    def __init__(self,passwd,host="localhost",port=6379):
        self.__redis = redis.StrictRedis(passwd=passwd,host=host,port=port)

    def set(self,key,value):
        self.__redis.set(key,value)

    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return " "

