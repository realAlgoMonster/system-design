## [Web Crawler](https://algo.monster/problems/system-design-web-crawler)

To run these code on your machine, you need to have python3 and pip installed. For Redis, you can [install](https://redis.io/topics/quickstart) on your machine, or use docker.

```
# install python dependency
pip install scrapy redis

# run redis from docker
docker run --name web-crawler-redis -p 6379:6379 -d redis

# start crawling
scrapy runspider spider.py
```
