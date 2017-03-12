import scrapy
import csv

class MinkaiSpider(scrapy.Spider):
    name = "minkai"

    def start_requests(self):
        urls = [
            'http://www.minnanokaigo.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_body = response.xpath('//*[@id="searchmap_list_block"]').css('a::attr(href)').extract()
        with open('ken_url.csv', 'w') as ken_url:
            writer = csv.writer(ken_url, lineterminator='\n') # 改行コード（\n）を指定しておく
            writer.writerow(page_body)     # list（1次元配列）の場合
            # writer.writerows(page_body)     # list（1次元配列）の場合
            # writer.writerows(array2d) # 2次元配列も書き込める
            for extracted_url in page_body:
                print(extracted_url)

        # page = response.url.split("/")[-2]
        page = response.url
        # filename = 'quotes-%s.html' % page
        filename = 'minkai.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
