#!/usr/bin/env python3
"""Writing to redis"""
import redis
import uuid
from typing import Union


class Cache(object):
    def __init__(self) -> None:
        """Instantiates a cache object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data into a redis db
        Params:
            data: can be str, bytes, int, float
        Returns: unique key generated
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
