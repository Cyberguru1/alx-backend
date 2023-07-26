#!/usr/bin/env python3
"""
FIFOCache
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """_summary_
        """
        BaseCaching.__init__(self)
    
    def put(self, key, item):
        """_summary_

        Args:
            key (value): index to store the content
            item (vaule): content to store
        """
        if key is None or item is None:
            pass

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            disKey = list(self.cache_data.keys())[0]
            print(f"DISCARD: {disKey}\n")
            del self.cache_data[disKey]

        self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]


