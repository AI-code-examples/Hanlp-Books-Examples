# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   IDEA
@Project    :   Hanlp-Books-Examples
@File       :   Trie.py
@Version    :   v0.1
@Time       :   2020-12-17 12:37
@License    :   (C)Copyright 2020-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""

from ch02.sec04.Node import Node


class Trie(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key):
        state = self
        for char in key:
            state = state._children.get(char)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        state = self
        for i, char in enumerate(key):
            if i < len(key) - 1:
                state = state._add_child(char, None, False)
            else:
                state = state._add_child(char, value, True)


def main():
    trie = Trie()

    # 增
    trie["自然"] = 'nature'
    trie["自然人"] = 'human'
    trie["自然语言"] = 'language'
    trie["自语"] = 'talk to oneself'
    trie["入门"] = 'introduction'
    print(trie["自然"])
    assert '自然' in trie

    # 删
    trie["自然"] = None
    print(trie["自然"])
    assert '自然' not in trie

    # 改
    trie["自然语言"] = 'human language'
    print(trie["自然语言"])
    assert trie["自然语言"] == 'human language'

    # 查
    print(trie["自然"])
    assert trie["入门"] == 'introduction'

    pass


if __name__ == '__main__':
    main()
