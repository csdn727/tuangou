#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from deal import Deal
from tuangou import Tuangou


class WWTuan(Tuangou):

    def __init__(self):
        api = "http://www.55tuan.com/openAPI.do?city=beijing"
        n = "55tuan"
        chname = '窝窝团'
        Tuangou.__init__(self, api=api, n=n, chname=chname)

    def parseDeals(self):

        items = self.json['response']['deals']['deal']
        for item in items:

            url = item['deal_url']
            title = item['title']
            cate = '-'

            d = {
                'title': title,
                'price': item['price'],
                'value': item['value'],
                'cate': cate,
                'subcate': '-',
                'url': url,
                'time': item["start_date"],
            }

            if self.timestamp > int(d['time']):
                continue

            deal = Deal().create_item(d)

            if len(deal.title) * len(deal.cate) == 0:
                continue

            self.deals.append(deal)


if __name__ == '__main__':
    WWTuan().start()
