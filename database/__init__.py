#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 14:28
# @Author  : Sakura
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from peewee import *

from configloader import *

if mysql_config['ssl_enable'] == 1:
    database = MySQLDatabase(mysql_config["db"],
                             host=mysql_config["host"], port=int(mysql_config["port"]),
                             user=mysql_config["user"], passwd=mysql_config["password"],
                             charset='utf8',
                             ssl={'ca': mysql_config["ssl_ca"], 'cert': mysql_config["ssl_cert"],
                                  'key': mysql_config["ssl_key"]}
                             )
else:
    database = MySQLDatabase(mysql_config["db"],
                             host=mysql_config["host"], port=int(mysql_config["port"]),
                             user=mysql_config["user"], passwd=mysql_config["password"],
                             charset='utf8'
                             )


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database

    def __repr__(self):
        return self._meta.clou


class SsNodeIp(BaseModel):
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    ip = TextField(null=True)
    node = IntegerField(column_name='node_id', constraints=[SQL("DEFAULT 0")])
    port = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = CharField(constraints=[SQL("DEFAULT 'tcp'")])

    class Meta:
        table_name = 'ss_node_ip'
