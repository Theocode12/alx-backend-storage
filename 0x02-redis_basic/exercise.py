#!/usr/bin/env python3
"""Use of Redis"""
from typing import Union
import redis
import uuid


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
