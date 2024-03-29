#!/usr/bin/env python3
"""
Contains the class RedisClient
"""
import redis


class RedisClient:
    """
    Interacts with the redis server
    """
    _client = None

    def __init__(self):
        """
        Instantiates a RedisClient object
        """
        self._client = redis.Redis()

    def isAlive(self):
        """
        Check whether is connected to the redis server
        """
        status = False
        try:
            status = self._client.ping()
        except:
            ...
        
        return status
    
    def get(self, key):
        """
        Retrieve a key from redis.
        """
        return self._client.get(key)

    def set(self, key, value, time):
        """
        Save a key to redis for a given time period
        Args:
            key (Any): the key of the value to store
            value (Any): the value to be stored
            time (int): time in seconds.
        """
        return self._client.setex(key, int(time), value)

    def delete(self, key):
        """
        Remove a key from the redis
        """
        return self._client.delete(key)
