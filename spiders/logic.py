# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from Pro_sp_37.items import ProSp37Item
from scrapy_splash import SplashRequest

class MeituSpider(scrapy.Spider):
    name = 'meitu'

    # cookies = {
    #     'cna': 'BmqJE2YVLzUCAXAC/gO80sws',
    #     'hng': 'CN%7Czh-CN%7CCNY%7C156',
    #     'thw:  cn, miid': '8247473821043720199',
    #     'tg:  0, t': 'a96fb47b68e059a74b394ed5d273c3dc',
    #     'enc': '0kGyal8B1CkZ79Rlb8j6osFz7xM363YjZnbv5G5JzPrERpSFfRpwJ7xR1PpRO%2Bg2FAWFdxy5dwC7hidBkh%2BmxQ%3D%3D',
    #     'x': 'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0',
    #     'cookie2': '162783593676bba0e365aaaeb2bdf05d',
    #     '_tb_token_': 'da7b8081e683',
    #     'swfstore': '196095',
    #     'JSESSIONID': '735CF67B01AA422BCECD6678664E50C2',
    #     'whl': '-1%260%260%261542279486266',
    #     'v': '0',
    #     'unb': '2641653084',
    #     'sg:  %E5%A4%B44b, _l_g_': 'Ug%3D%3D',
    #     'cookie1': 'U7enPFjZg4oR99T5hj90bbdqZQ%2FcNIbh%2B3ksxyEuvsc%3D',
    #     'tracknick': '%5Cu9047%5Cu6C34%5Cu5730%5Cu77F3%5Cu5934',
    #     'lgc': '%5Cu9047%5Cu6C34%5Cu5730%5Cu77F3%5Cu5934',
    #     'dnk': '%5Cu9047%5Cu6C34%5Cu5730%5Cu77F3%5Cu5934',
    #     '_nk_': '%5Cu9047%5Cu6C34%5Cu5730%5Cu77F3%5Cu5934',
    #     'cookie17': 'UU6lTMBtFjit3A%3D%3D',
    #     'mt': 'ci=5_1&np=',
    #     'skt': 'f24b342e7407bb7a',
    #     'csg': '375fc41a',
    #     'uc3': 'vt3=F8dByR%2FCmA5O4VKLdsk%3D&id2=UU6lTMBtFjit3A%3D%3D&nk2=sHb34ZZ4OMmZnA%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D',
    #     'existShop': 'MTU0MjI3OTg3OQ%3D%3D',
    #     '_cc_': 'Vq8l%2BKCLiw%3D%3D',
    #     'uc1': 'cookie14=UoTYNO0pAK7Rsg%3D%3D&lng=zh_CN&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&cookie21=UIHiLt3xThH8t7YQoFNq&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0',
    #     'isg': 'BFRUDGfb8-o5HWdNIOZIrGpMJZLMpmAoNIHCP-41ol9i2fQjFr1IJwoQ3dHBIbDv',
    #
    # }
    cookie_str = "cna=BmqJE2YVLzUCAXAC/gO80sws; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=8247473821043720199; tg=0; t=a96fb47b68e059a74b394ed5d273c3dc; enc=0kGyal8B1CkZ79Rlb8j6osFz7xM363YjZnbv5G5JzPrERpSFfRpwJ7xR1PpRO%2Bg2FAWFdxy5dwC7hidBkh%2BmxQ%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; tracknick=%5Cu9047%5Cu6C34%5Cu5730%5Cu77F3%5Cu5934; lgc=%5Cu9047%5Cu6C34%5Cu5730%5Cu77F3%5Cu5934; mt=ci=5_1&np=; uc3=vt3=F8dByR%2FCmA5O4VKLdsk%3D&id2=UU6lTMBtFjit3A%3D%3D&nk2=sHb34ZZ4OMmZnA%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; _cc_=Vq8l%2BKCLiw%3D%3D; JSESSIONID=561E5DE3BAA14B586EA93AB74732733F; swfstore=203854; v=0; cookie2=1c4d2296bfa11a2c4a968a1b43cc3f73; _tb_token_=f603de3b5b393; isg=BNTUgK_3c2l4qefNoGbILOrMpRJMJuTLtAFCv261AN_iWXSjlj5Kp4rTXRHkoTBv; uc1=cookie14=UoTYNOyJYelDvQ%3D%3D"
    cookies_dict = {

    }
    for item in cookie_str.split('; '):
        cookies_dict[item.split('=', maxsplit=2)[0]] = item[len(item.split('=', maxsplit=2)[0])+1:]
    print(cookies_dict)
    cookies = cookies_dict
    allowed_domains = ['s.taobao.com']
    start_urls = ['https://s.taobao.com/list?q=%E5%A4%A7%E8%A1%A3']
    headers = {
        'upgrade-insecure-requests': 1


    }

    def start_requests(self):
        yield SplashRequest(url=self.start_urls[0], callback=self.parse, cookies=self.cookies, args={'wait': '0.5'},)

    def parse(self, response):
        print('yes')
        goods = response.xpath(".//div[@class='item J_MouserOnverReq  item-sku J_ItemListSKUItem']")
        print(goods)
        for each in goods:
            item = ProSp37Item()
            item['img_link'] = each.xpath(".//img[@class='J_ItemPic img']//@src").extract()
            item['goods_name'] = each.xpath("//img[@class='J_ItemPic img']/@alt").extract()
            item['goods_link'] = each.xpath("//img[@class='J_ItemPic img']/../@href").extract()
            item['goods_price'] = each.xpath("//div[@class='price g_price g_price-highlight']/strong").extract()
            item['shop_link'] = each.xpath("//div[@class='row row-3 g-clearfix']//a[@class='shopname J_MouseEneterLeave J_ShopInfo']/@href").extract()
            item['shop_name'] = each.xpath("//div[@class='row row-3 g-clearfix']//a[@class='shopname J_MouseEneterLeave J_ShopInfo']/span[2]/text()").extract()
            item['shop_area'] = each.xpath("//div[@class='row row-3 g-clearfix']/div[@class='location']/text()").extract()
            item['purchase_num'] = each.xpath("//div[@class='row row-1 g-clearfix']/div[@class='deal-cnt']/text()").extract()
            item['post_included'] = each.xpath("//div[@class='row row-2 title']//span[@class='baoyou-intitle icon-service-free']/@class").extract()
            yield item

        with open('text.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
