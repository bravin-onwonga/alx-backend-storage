#!/usr/bin/env python3
"""Writing to redis"""
import redis
import uuid
from typing import Union, Callable, Optional

@decorator
def count_calls(method: Callable) -> Callable:
    """Incrementing values in redis"""
    key = method.__qualname__


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
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[Union[str, int], [str, int]]]):
        """Reading from Redis and recovering original type"""
        value: Union[str, bytes, int, float] = self._redis.get(key)
        if fn == int:
            value: int = self.get_int(value)
        elif fn is None or fn == str:
            value: str = self.get_str(value)
        else:
            value: Union[str, bytes, int, float] = fn(value)

        return value

    def get_str(self, vaue: bytes):
        """Automatically parametrize Cache.get with
        the correct conversion function"""
        return str(value)

    def get_int(self):
        """Automatically parametrize Cache.get with
        the correct conversion function"""
        return str(value)
