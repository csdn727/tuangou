#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author  : Rex Zhang
# datetime: 2012-08-10 08:09:40
# filename: main.py


from meituan import Meituan
from dianping import Dianping
from lashou import Lashou
from nuomi import Nuomi
from wwtuan import WWTuan
from ftuan import FTuan
from tuanbao import Tuanbao
from tongcheng import Tongcheng
from didatuan import Didatuan
from settings import logger


def main():
    logger.info("")
    logger.info("Main program started...")
    for cls in (Dianping, Meituan, Lashou, Nuomi, WWTuan, FTuan, Tuanbao,
                Tongcheng, Didatuan):
        cls().start()

if __name__ == '__main__':
    main()
