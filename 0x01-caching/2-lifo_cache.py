#!/usr/bin/python3
""" Apply algorithm LIFOCache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class inherits from BaseCaching"""

    def __init__(self):
        """ Initialize a new object """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.order.pop()
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
