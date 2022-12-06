#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import time

tree = ET.parse('./orders.xml')
root = tree.getroot()
orders = {'book-2': [], 'book-1': [], 'book-3': []}


def handleOrder(attributes):
    for item in orders[attributes.book]:
        if item['orderId'] == attributes['orderId']:
            new_dict = {}
            new_dict[attributes['operation'
                     ]].push({'volume': attributes['volume'],
                             'price': attributes['price']})
            item['data'].push(new_dict)
        else:
            new_item = {}
            new_dict = {}
            new_dict[attributes['operation'
                     ]].push({'volume': attributes['volume'],
                             'price': attributes['price']})
            new_item['data'].push(new_dict)
            orders[attributes.book]


def main():
    startTime = time.time()
    for child in root:
        if attributes['tag'] == 'DeleteOrder':
            for item in orders[attributes.book]:
                orders[attributes.book] = list(filter(lambda score: \
                        score['orderId'] != attributes['orderId'],
                        orders[attributes.book]))
        else:
            handleOrder(attributes)

    for (book, data) in orders.items():
        print book
        for item_ in data:
            print item_['buy']['volume'] + '@' + item['price'] + '---' \
                + item_['sell']['volume'] + '@' + item['price']
    print 'TIME ELAPSED' + time.time() - startTime
