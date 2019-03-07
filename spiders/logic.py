# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from Pro_sp_37.items import ProSp37Item
from scrapy_splash import SplashRequest

class LogicSpider(scrapy.Spider):
    name = 'logic'
    allowed_domains = ['weibo.com']
    start_urls = ['https://weibo.com/u/6942689016/home?topnav=1&wvr=6']
    cookies = {'SINAGLOBAL': '517576600038.92926.1527168713268',
               'SUB': '_2A25xhOTuDeRhGeBH71AX-CfMyjqIHXVS8FEmrDV8PUJbmtAKLRjGkW9NQdXIW22dPuz3vT2H0wlYQXEI3i6EvF9p',
               'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5OXqSp9S-SBpNYcFGCPc5L5NHD95Qc1KBESon4eh2cWs4Dqcj_i--fiKnci-\
               zEi--fiK.fiKyWi--RiKn7iKnpi--fi-2Xi-zXi--fi-82iK.7',
               'SUHB': '0LcSdGbbWCLyKh',
               'ALF': '1583466559',
               'SSOLoginState': '1551930559',
               'Ugrow-G0': 'ea90f703b7694b74b62d38420b5273df',
               'wvr': '6',
               'YF-V5-G0': 'da1eb9ea7ccc47f9e865137ccb4cf9f3',
               '_s_tentry': 'www.sina.com.cn',
               'UOR': ',,www.sina.com.cn',
               'Apache': '5261344978846.561.1551930572416',
               'YF-Page-G0': '00acf392ca0910c1098d285f7eb74a11',
               'ULV': '1551930572444:14:1:1:5261344978846.561.1551930572416:1546324449262',
               'wb_view_log_6942689016': '1920*10801',
               'webim_unReadCount': '%7B%22time%22%3A1551930677622%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%\
               2C%22allcountNum%22%3A34%2C%22msgbox%22%3A0%7D'
               }

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse, cookies=self.cookies, args={'wait': '0.5'},)

    def parse(self, response):
        print('remote ...')

        with open('text.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
