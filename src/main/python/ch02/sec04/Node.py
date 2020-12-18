# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   IDEA
@Project    :   Hanlp-Books-Examples
@File       :   Node.py
@Version    :   v0.1
@Time       :   2020-12-17 12:41
@License    :   (C)Copyright 2020-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""


class Node(object):
    def __init__(self, value) -> None:
        self._children = {}
        self._value = value

    def _add_child(self, char, value, overwrite=False):
        child = self._children.get(char)
        if child is None:
            child = Node(value)
            self._children[char] = child
        elif overwrite:
            child._value = value
        return child
