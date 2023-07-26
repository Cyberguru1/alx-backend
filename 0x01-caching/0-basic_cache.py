#!/usr/bin/env python3
""" BaseCaching Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
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
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
