#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

"""
 DESCRIPTION:
"""

class MyHashSet(object):

    def __init__(self):
        self.__dummy = True
        self.data = dict()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.data[key] = self.__dummy


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.data:
            del self.data[key]


    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.data



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)