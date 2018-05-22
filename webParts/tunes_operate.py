import redis
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


def operate_snapshot():
    redis_conn.set("snapshot", 1)


def operate_makemovie():
    redis_conn.set("makemovie", 1)


def operate_quit():
    redis_conn.set("quit", 1)


def operate_restart():
    redis_conn.set("restart", 1)