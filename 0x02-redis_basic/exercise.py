#!/usr/bin/env python3
"""Writing to redis"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str,
            fn: Optional[Callable[Union[str, int], [str, int]]]):
        """Reading from Redis and recovering original type"""
        value = self._redis.get(key)
        if fn == int:
            value = self.get_int(value)
        elif fn is None:
            value = self.get_str(value)
        else:
            value = fn(value)

        return value

    def get_str(self, vaue: bytes):
        """Automatically parametrize Cache.get with
        the correct conversion function"""
        return str(value)

    def get_int(self):
        """Automatically parametrize Cache.get with
        the correct conversion function"""
        return str(value)
