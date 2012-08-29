#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author  : Rex Zhang
# datetime: 2012-08-18 13:22:46
# filename: settings.py

from logger import Logger
logger = Logger().getLogger()

DEBUG = False
enable_sending = True

mailer_args = {
    "host": 'localhost',
    "port": 25,
    'username': '',
    'password': '',
    'frm': 'rex',
    'to': 'rex@zhasm.com',
    'subject': '%s 每日新单 on %s',
    'title': '',
    'fs': r'\s+',
    'max_split': 0,
    'header': '货物 售价 原价 大类 小类 链接',
}


try:
    #the structure of local_settings is identical with settings.
    #force load local setting if any, to override default setting.
    #using local setting at high privilege
    from local_settings import DEBUG, mailer_args
except ImportError as e:
    logger.error(e)
