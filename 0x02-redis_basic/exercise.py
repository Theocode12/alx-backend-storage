#!/usr/bin/env python3
"""Use of Redis"""
from typing import Union, Callable
import redis
import uuid
import sys


class Cache(object):
    """Cache class"""
    def __init__(self):
        """cache constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and returns the key"""
        key = uuid.uuid4().__str__()
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Union[Callable[[bytes], Union[str, bytes, int, float]],
                      None] = None):
        """Get the value in the original format"""
        value = self._redis.get(key)
        if value and callable(fn):
            value = fn(value)
        return value

    def get_str(self, value: bytes):
        """Get the str value in the original format"""
        return value.decode('utf-8')

    def get_int(self, value: bytes):
        """Get the int value in the original format"""
        return int.from_bytes(value, sys.byteorder)
