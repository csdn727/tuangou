#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author  : Rex Zhang
# datetime: 2012-08-10 14:55:03
# filename: meituan.py

from deal import Deal
from tuangou import Tuangou
from xml2json import ensureAscii


class Meituan(Tuangou):

    def __init__(self):
        api = "http://www.meituan.com/api/v2/beijing/deals"
        n = "meituan"
        chname = '美团'
        Tuangou.__init__(self, api=api, n=n, chname=chname)

    def parseDeals(self):

        assert self.json

        items = self.json['response']['deals']['data']

        for item in items:
            item = item['deal']

            d = {
                'title': ensureAscii(item['deal_title']),
                'price': item['price'],
                'value': item['value'],
                'cate': ensureAscii(item['deal_cate']),
                'subcate': ensureAscii(item['deal_subcate']),
                'url': ensureAscii(item['deal_url']),
                'time': item["start_time"],
            }

            if self.timestamp > int(d['time']):
                continue
            deal = Deal().create_item(d)
            self.deals.append(deal)

if __name__ == '__main__':
    Meituan().start()
