#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 13:59
# @Author  : Sakura
# @Site    : 
# @File    : net_util.py
# @Software: PyCharm


def from_map_ipv6_get_ipv4(address):
    if address.startswith("::ffff:"):
        return address[7:]
    if address.startswith("0:0:0:0:0:ffff:"):
        return address[15:]

