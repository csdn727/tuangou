#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from deal import Deal
from tuangou import Tuangou


class Tongcheng(Tuangou):

    def __init__(self):
        #cityID=2 means beijing
        api = "http://open.t.58.com/api/products?city=bj"
        n = "58tuan"
        chname = '58同城团'
        Tuangou.__init__(self, api=api, n=n, chname=chname)

    def parseDeals(self):

        assert self.json

        items = self.json['urlset']['url']

        for item in items:

            url = item['loc']
            item = item['data']['display']

            d = {
                'title': item['title'],
                'price': item['price'],
                'value': item['value'],
                'cate': item['category'],
                'subcate': item['tag'],
                'url': url,
                'time': item["startTime"],
            }

            if self.timestamp > int(d['time']):
                continue

            deal = Deal().create_item(d)
            if len(deal.title) * len(deal.cate) * len(deal.subcate) == 0:
                continue

            self.deals.append(deal)

if __name__ == '__main__':
    Tongcheng().start()
