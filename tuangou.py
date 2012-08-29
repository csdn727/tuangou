#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
from settings import DEBUG, mailer_args, logger, enable_sending
from threading import Thread
from xml2json import xml2json
from util import time_convert, multikeysort
from htmler import msg
import requests


class virt(object):
    pass


class Tuangou(Thread):
    ''' list of deals '''

    def __init__(self, n, api='', chname=''):  # n==name

        Thread.__init__(self)
        self.api = api
        self.name = n
        self.chname = chname
        self.json = {}
        self.deals = []
        self.timestamp, self.datestring = time_convert()
        self.args = virt()
        self.log = logger

        for (k, v) in mailer_args.items():
            setattr(self.args, k, v)

        self.args.subject %= (self.chname, self.datestring)

    def _sort(self):

        self.deals = multikeysort(self.deals, ['cate',
                                               'subcate',
                                               '-value',
                                               '-price',
                                               'url'])

    def download(self):
        if DEBUG:
            raw = open(self.name + '.xml').read()
        else:
            self.log.info("%s begins to download xml" % self.name)
            raw = requests.get(self.api).content
            self.log.info("%s download xml finished %d" % (
                self.name, len(raw)))

        self.json = json.loads(xml2json(raw))
        assert self.json

    def parseDeals(self):
        return NotImplemented

    def stat(self):
        if self.deals:

            def _int(x):
                try:
                    return int(x)
                except ValueError as e:
                    self.log.error(e)
                    return 0

            number = len(self.deals)
            sum_price = sum([_int(d.price) for d in self.deals])
            sum_value = sum([_int(d.value) for d in self.deals])
            avg_price = sum_price / number
            avg_value = sum_value / number
            return "总价：%d; 总值：%d; 均价：%d; 均值：%d" % \
                    (sum_price, sum_value, avg_price, avg_value)

    def output(self):
        return [str(deal) for deal in self.deals]

    def run(self):

        self.log.info("%s begin to run." % self.name)
        self.download()
        self.parseDeals()

        if hasattr(self, 'page'):
            self.api += "/p/2"
            self.download()
            self.parseDeals()

        self._sort()
        lines = self.output()
        self.args.lines = lines

        if len(lines):
            self.args.title = "今日新单数： %d; %s" % (len(lines), self.stat())
        else:
            self.args.title = '今日无新单。'
            self.args.header = ''

        self.log.info("%s begin to send mail." % self.name)
        if enable_sending:
            msg(self.args)
        self.log.info("%s mail sent ok" % self.name)
