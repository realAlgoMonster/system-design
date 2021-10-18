## [Tiny URL Shortener](https://algo.monster/problems/system-design-tiny-url-shortener)

To run these code on your machine, you need to have python3 and pip installed. For Redis, you can use cloud services like [AWS](https://aws.amazon.com/redis/), [install](https://redis.io/topics/quickstart) on your machine, or use docker.

```
# install python dependency
pip install flask redis

# run redis from docker
docker run --name tiny-url-shortener-redis -p 6379:6379 -d redis

# start web server
FLASK_APP=. flask run
```
