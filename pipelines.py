# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProSp37Pipeline(object):


    def process_item(self, item, spider):
        print('pipline')
        json_f = open('./info.json', 'w')
        print(len(item['goods_name']))
        for i in range(0, len(item['goods_name'])):
            goods = {
                #'img_link': item['img_link'][i],
                # 商品名称
                'goods_name': item['goods_name'][i],
                # 商品链接
                'goods_link': item['goods_link'][i],
                # 商品价格
                'goods_price': item['goods_price'][i],
                # 所属店家
                'shop_name': item['shop_name'][i],
                # 店家链接
                'shop_link': item['shop_link'][i],
                # 所属地区
                'shop_area': item['shop_area'][i],
                # 购买人数
                'purchase_num': item['purchase_num'][i],
            }
            print(goods)
            goods_json = json.dumps(dict(goods), ensure_ascii=False) + '\n'
            json_f.write(goods_json)
        json_f.close()
        return item
