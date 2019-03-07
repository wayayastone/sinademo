# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProSp37Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 商品图片
    img_link = scrapy.Field()
    # 商品名称
    goods_name = scrapy.Field()
    # 商品链接
    goods_link = scrapy.Field()
    # 商品价格
    goods_price = scrapy.Field()
    # 所属店家
    shop_name =  scrapy.Field()
    # 店家链接
    shop_link = scrapy.Field()
    # 所属地区
    shop_area = scrapy.Field()
    # 购买人数
    purchase_num = scrapy.Field()
    # 是否包邮
    post_included = scrapy.Field()

