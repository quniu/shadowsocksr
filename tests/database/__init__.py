#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/27 15:16
# @Author  : Sakura
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm

import logging
import unittest

from playhouse.shortcuts import model_to_dict

from database import *


class MyTestCase(unittest.TestCase):
    def test_ss_node_ip(self):
        ss = SsNodeIp(ip="192.168.1.1", port=3306, type="tcp", create_at=None)
        ss.save()
        ss_list = SsNodeIp.select(SsNodeIp.port == 3306)
        logging.info(list([model_to_dict(x) for x in ss_list]))
        self.assertTrue(len(ss_list) > 0)
        query = SsNodeIp.delete()
        query.execute()


if __name__ == '__main__':
    unittest.main()
