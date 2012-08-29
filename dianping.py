#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from deal import Deal
from tuangou import Tuangou
from xml2json import ensureAscii


class Dianping(Tuangou):

    def __init__(self):
        #cityID=2 means beijing
        api = "http://api.t.dianping.com/n/api.xml?cityId=2"
        n = "dianping"
        chname = '大众点评'
        Tuangou.__init__(self, api=api, n=n, chname=chname)

    def parseDeals(self):

        assert self.json

        items = self.json['urlset']['url']

        for item in items:

            url = item['loc']
            item = item['data']['display']

            d = {
                'title': item['shortTitle'],
                'price': item['price'],
                'value': item['value'],
                'cate': item['category'],
                'subcate': item['subcategory'],
                'url': url,
                'time': item["startTime"],
            }

            if ensureAscii(item['city']) not in ['北京', '全国']:
                continue

            if self.timestamp > int(d['time']):
                continue

            deal = Deal().create_item(d)
            if len(deal.title) * len(deal.cate) * len(deal.subcate) == 0:
                continue

            self.deals.append(deal)
