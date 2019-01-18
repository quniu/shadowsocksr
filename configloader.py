#!/usr/bin/python
# -*- coding: utf-8 -*-
import importloader
from utils.json_util import *
import os

g_config = None
mysql_config = None

def load_config():
    global g_config
    g_config = importloader.loads(['userapiconfig', 'apiconfig'])


def load_mysql_config():
    global mysql_config
    tmp = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "ss",
        "password": "pass",
        "db": "shadowsocks",
        "node_id": 0,
        "transfer_mul": 1.0,
        "ssl_enable": 0,
        "ssl_ca": "",
        "ssl_cert": "",
        "ssl_key": ""}
    config_path = g_config.MYSQL_CONFIG
    with open(os.path.join(os.path.split(__file__)[0],config_path), 'rb+') as f:
        cfg = JsonUtil.json_loads(f.read().decode('utf8'))
    tmp.update(cfg)
    mysql_config = tmp


def get_config():
    return g_config


def get_mysql_config():
    return mysql_config


load_config()
load_mysql_config()

