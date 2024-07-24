#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = {}
        self.order = {}
        self.min_freq = 0

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            freq = self.frequency[key]
            self.order[freq - 1].remove(key)
            if freq not in self.order:
                self.order[freq] = []
            self.order[freq].append(key)
            if not self.order[self.min_freq]:
                self.min_freq += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_keys = self.order[self.min_freq]
                if lfu_keys:
                    lfu_key = lfu_keys.pop(0)
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print("DISCARD:", lfu_key)
                if not self.order[self.min_freq]:
                    del self.order[self.min_freq]
                    self.min_freq += 1
            
            self.cache_data[key] = item
            self.frequency[key] = 1
            if 1 not in self.order:
                self.order[1] = []
            self.order[1].append(key)
            self.min_freq = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.frequency[key] += 1
        freq = self.frequency[key]
        self.order[freq - 1].remove(key)
        if freq not in self.order:
            self.order[freq] = []
        self.order[freq].append(key)
        
        if not self.order[self.min_freq]:
            del self.order[self.min_freq]
            self.min_freq += 1

        return self.cache_data[key]
