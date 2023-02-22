#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# @author: liuxiji
# @time: 2023/02/22 16:20:24

"""
 DESCRIPTION: 链表的helper
"""

class ListNode(object):
    """ 链表的Node
    """
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def append(target, val):
    """append"""
    if target is None:
        return ListNode(val)

    target.next = ListNode(val)
    return target.next


def build(lst):
    """build"""
    header = ListNode(-1, None)

    trailer = header
    for x in lst:
        trailer = append(trailer, x)

    return header.next


def to_vec(lst):
    """to vector"""
    vec = []
    while lst is not None:
        vec.append(lst.val)

        lst = lst.next
    return vec


def debug_print(lst):
    """print"""
    vec = to_vec(lst)
    print(vec)