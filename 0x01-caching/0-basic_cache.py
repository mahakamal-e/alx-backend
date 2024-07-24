#!/usr/bin/python3
"""
Create a class BasicCache that inherits from BaseCaching,
and is a caching system
"""
from base_caching import BaseCaching


class BaseCaching(BaseCaching):
    """ Implement Class BaseCaching """
    def __init__(self):
        """initialize new object"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
