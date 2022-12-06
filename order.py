#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import time,json

tree = ET.parse('./orders.xml')

orders = {'book-2': {}, 'book-1':{}, 'book-3': {}}
def handleOrder(attributes):
    if str(attributes['orderId']) in orders[attributes['book']]:
        orders[attributes['book']][str(attributes['orderId'])][attributes['operation']].push(
                {'volume': attributes['volume'],
                 'price': attributes['price']})
    else:
       orders[attributes['book']][str(attributes['orderId'])] = {
            attributes['operation']: [{'volume': attributes['volume'],
                                       'price': attributes['price']}]
          }

def main():
    root = tree.getroot()
    startTime = time.time()
    for child in root:
        attrs = child.attrib
        if child.tag == 'DeleteOrder':
            orderId = str(attrs['orderId'])
            if orderId in orders[attrs['book']]:
                del orders[attrs['book']][orderId]
        else:
            handleOrder({'book': attrs['book'], 'operation': attrs['operation'], 'price':attrs['price'],'volume':attrs['volume'], 'orderId':attrs['orderId']})
    with open("output.json", "w") as outfile:
        outfile.write(json.dumps(orders, indent=4))
    print('TIME ELAPSED' + str(time.time()-startTime))

main()