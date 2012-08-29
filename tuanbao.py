#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from deal import Deal
from tuangou import Tuangou


class Tuanbao(Tuangou):

    def __init__(self):
        api = "http://p5.groupon.cn/xml/city/cityproduct/?cityid=1"
        n = "tuanbao"
        chname = '团宝'
        Tuangou.__init__(self, api=api, n=n, chname=chname)

    def parseDeals(self):

        items = self.json['urlset']['url']
        for item in items:

            url = item['loc']
            item = item['data']['display']
            title = item['title']
            cate = '-'

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
    Tuanbao().start()
