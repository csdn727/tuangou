#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from deal import Deal
from tuangou import Tuangou


class Lashou(Tuangou):

    def __init__(self):
        #2419==beijing means beijing
        api = "http://open.client.lashou.com/api/detail/city/2419"
        n = "lashou"
        chname = '拉手'
        self.page = True
        Tuangou.__init__(self, api=api, n=n, chname=chname)

    def parseDeals(self):

        items = self.json['urlset']['url']
        for item in items:

            url = item['loc']
            item = item['data']['display']
            title = item['title']
            cate = item['cate']

            d = {
                'title': title,
                'price': item['price'],
                'value': item['value'],
                'cate': cate,
                'subcate': '-',
                'url': url,
                'time': item["startTime"],
            }

            if self.timestamp > int(d['time']):
                continue

            deal = Deal().create_item(d)

            if len(deal.title) * len(deal.cate) == 0:
                continue

            self.deals.append(deal)

if __name__ == '__main__':
    Lashou().start()
