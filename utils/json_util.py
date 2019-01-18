#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 13:59
# @Author  : Sakura
# @Site    : 
# @File    : net_util.py
# @Software: PyCharm
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return JSONEncoder.default(self, obj)
        if isinstance(obj, set):
            return list(obj)


def as_python_object(dct):
    if '_python_object' in dct:
        return pickle.loads(str(dct['_python_object']))
    return dct


class JsonUtil(object):
    @classmethod
    def dumps(cls, obj):
        """
        序列化python对象到json字符串
        :param obj:
        :return:
        """
        return dumps(obj, cls=PythonObjectEncoder)

    @classmethod
    def json_loads(cls, str):
        """
        反序列化json字符串到python对象
        :param str:
        :return:
        """
        return loads(str, object_hook=as_python_object)

