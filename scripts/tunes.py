import redis
import requests
import time
import os

SNAPSHOTURL = ""
MAKEMOVIEURL = ""

UPLOAD_PATH = os.path.dirname(__file__)
redis_config = {
    "host": "118.25.42.123",
    "port": 6379
}
# redis连接对象
redis_pool = redis.ConnectionPool(**redis_config)
redis_conn = redis.Redis(connection_pool=redis_pool)

while True:
    snap = redis_conn.get("snapshot")
    if snap == '1':
        requests.get(SNAPSHOTURL)
        redis_conn.set("snapshot", 0)
    movie = redis_conn.get("makemovie")
    if movie == '1':
        requests.get(MAKEMOVIEURL)
        redis_conn.set("makemovie", 0)
