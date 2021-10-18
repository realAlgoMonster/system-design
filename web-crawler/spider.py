import scrapy
from urllib.parse import urlparse
from scrapy.linkextractors import LinkExtractor
import redis
import os
import time
from pathlib import Path


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    le = LinkExtractor()
    r = redis.Redis(host='localhost', port=6379, db=0)
    path = 'data'
    hostname = ''

    def start_requests(self):
        # init task queue with a URL
        self.r.rpush('task_queue', 'http://quotes.toscrape.com/page/1/')

        while True:
            item = self.r.lpop('task_queue')
            if item is None:
                time.sleep(1)
                item = self.r.lpop('task_queue')
                if item is None:
                    break
            url = item.decode("utf-8")
            if self.hostname == '':
                self.hostname = urlparse(url).hostname
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filepath = urlparse(response.url).path
        if filepath[-1] == '/':
            filepath += 'index.html'
        path = self.path + filepath
        Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            f.write(response.body)

        self.r.sadd('task_finished', response.url)

        for link in self.le.extract_links(response):
            url = link.url
            if urlparse(url).hostname != self.hostname:
                continue
            if self.r.sismember('task_finished', url):
                continue
            self.r.rpush('task_queue', url)
