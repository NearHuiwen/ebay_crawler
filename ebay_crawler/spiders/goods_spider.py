# -*- coding: utf-8 -*-
# @Author : lihuiwen
# @file : goods_spider
# @Email : huiwennear@163.com
# @Time : 2024/5/23 14:00
from urllib.parse import urljoin

import scrapy
from scrapy import Request


class GoodsSpider(scrapy.Spider):
    name = "goods_spider"

    def __init__(self):
        self.req_headers = {
            'sec-ch-ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-full-version': '"22.1.1090.64"',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-model': '""',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.160 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'ak_bmsc=14620A30FBD46F7B58A32116F82F1ED9~000000000000000000000000000000~YAAQxZTYF8nZn6mPAQAAghf7qReXZEwwNX4F7qDt0VQFbLNkAltLot5MUlppG/e5g0I7Jqw3kfgdzzIQPiVYNcXlc7FIwjag8P3RNJ05BddgMNmtNSTvkn07FtenrN+tc4CDBDTzeZH5aEMcXz/Rfc7ezpoKlxdn7bb27MTKxmTPvI4PnAwkEbYf470/3W1x00L+H5q050b1P1cTgJxHoxhHPH3MoMMV6ZTWSywvg9aXAwsx5WvSk2nloKa6pvy6JF7/z+U1+CCtKiyZgC/QcPdNgluO6V32S5f+O2ymXveLEwZDBPXq4UcYDCEo/J7KMGOI2H3KZ9tX1HCuy9JM4w5yldyCMLpWqcIrowooOC59Au4Cu8+rKNN0fjSSCbZ4qT5Kxsk=; __uzma=a3b39c27-1cdb-416c-9d4a-a77b8bf98d1b; __uzmb=1716543756; __uzme=9841; AMP_MKTG_f93443b04c=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tLmhrJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tLmhrJTIyJTdE; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=d90548bd-4934-4b3f-9d69-382e535517f8; __uzmbj2=1716543847; __gsas=ID=a36409458aa81293:T=1716543855:RT=1716543855:S=ALNI_MaysvDc8VwdqqGjCh-yrhiGAKWA-A; __gads=ID=a7b5d3bb52abebab:T=1716543851:RT=1716544638:S=ALNI_MbNdA8kklA_-FJLdxrOuQF9l1jBpg; __gpi=UID=00000e2b3d2bdfb9:T=1716543851:RT=1716544638:S=ALNI_MaynHvxWnkA1dVNvd_h_ZIa1-W8Rw; __eoi=ID=ac3443b912c4247b:T=1716543851:RT=1716544638:S=AA-AfjZqWxpNWCH0BdO_vIeCqPgG; __uzmcj2=337631996147; __uzmdj2=1716544653; AMP_f93443b04c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5MDU0YzVlNi01MTQzLTRjMWEtOWQ0Zi02MTViOWFjMjAxNjQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE2NTQzNzU3ODA5JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNjU0NDY1NTQ3MiUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTIlMkMlMjJwYWdlQ291bnRlciUyMiUzQTExJTdE; s=CgAD4ACBmUbX7YTlmYjE3NTAxOGYwYWI4ZTRmZjc0Y2UyZmZmZWVmYWJiLz86; ns1=BAQAAAY5O25hEAAaAANgAU2gxmBFjNjl8NjAxXjE3MTY1NDM4NDY5MDheXjFeM3wyfDV8NHw3fDEwfDQyfDQzfDExXl5eNF4zXjEyXjEyXjJeMV4xXjBeMV4wXjFeNjQ0MjQ1OTA3NaXO+qb8Q3Rq+1QDG5ltoBRGal5D; nonsession=BAQAAAY5O25hEAAaAADMAAWgxmBEwAMoAIGoSy5FhOWZiMTc1MDE4ZjBhYjhlNGZmNzRjZTJmZmZlZWZhYgDLAAJmUGuZNDLWoqnzobyoKEmmtR4kjacvPgW2nA**; dp1=bu1p/QEBfX0BAX19AQA**6a12cb91^pbf/%23e000e0000000000000000068319811^bl/HK6a12cb91^; __deba=j3RW-S2cmjlTaAdJFkqMJ77s9Xgb-AMz6kkNhZ9PTFI3a-QFNapTz_Ho86xM1c7qhCQI0BjOpXU2T8FBYLbLt0cjrAMBI1G2Yo9kDD-C-TSeAJZf1y_-ElOFErRH1r_V7S8ONStp7eYq8xGYOesx5Q==; __uzmc=391542851020; __uzmd=1716544657; __uzmf=7f600054b04c17-bff1-4eaf-aa51-196aa53cda581716543756846900546-981fb79c63f6c6ea28; bm_sv=FE0D38F5DDA39B7618C2B10C0A91F4AC~YAAQ2ZTYF3kA5pSPAQAAbNsIqheu53lSG1aONzL1GY7SOJt5A+MiYZwfutTSt9h/YC2aq8hyZqBqDsUbY8H5+2cEHfJIIMPzlI1xF9z9ecVitX6QaKpIvK+sLBJHQZ5q8SdIGaJCjttkTRGISorozoRVoYTBhvOfsFeq43pBg+VrUQyfaRC5VH79p2C1kIWQi+CsH6WpvhjCClVGa3d2WrMlDjUJbbjB2RU4t6D5+ZD2sdwd7R4nhM5GJIDsmos=~1; ebay=%5Ejs%3D1%5Esbf%3D%23000000%5Epsi%3DACMZZGas*%5E; ds2=sotr/b8_5az10JNfz^',
        }

        self.proxy = ""

    def start_requests(self):
        keyword = "iphone"
        page = 1
        req_url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={keyword}&_sacat=0&_pgn={page}'
        req_meta = {"keyword": keyword, "page": page,
                    # "proxy":self.proxy
                    }
        yield Request(url=req_url, method='GET', headers=self.req_headers,
                      callback=self.detail_page_parse, meta=req_meta,
                      dont_filter=True)

    def detail_page_parse(self, response):
        keyword = response.meta.get('keyword')
        page = response.meta.get('page')
        div_list = response.xpath('//a[string-length(@data-interactions) > 0 and div[@class="s-item__title"]]')
        if (div_list):
            for div_index in range(1,len(div_list)):

                div_item = div_list[div_index]
                goods_item = {}

                goods_item["detail_url"] = urljoin("https://www.ebay.com/", div_item.xpath(
                    './@href').extract_first().strip())
                req_meta = {"keyword": keyword, "goods_item": goods_item,
                            # "proxy":self.proxy
                            }
                yield Request(url=goods_item["detail_url"], method='GET', headers=self.req_headers,
                              callback=self.detail_parse, meta=req_meta,
                              dont_filter=True)
            page += 1
            req_url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={keyword}&_sacat=0&_pgn={page}'
            req_meta = {"keyword": keyword, "page": page,
                        # "proxy":self.proxy
                        }
            yield Request(url=req_url, method='GET', headers=self.req_headers,
                          callback=self.detail_page_parse, meta=req_meta,
                          dont_filter=True)
        else:
            print("没有下一页")

    def detail_parse(self, response):
        keyword = response.meta.get('keyword')
        goods_item = response.meta.get('goods_item')
        goods_item["name"] = response.xpath('//h1[@class="x-item-title__mainTitle"]/span/text()').extract_first().strip()
        goods_item["goods_price"] = response.xpath('//div[@class="x-price-primary"]/span/text()').extract_first().strip()
        print(goods_item)
