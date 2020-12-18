# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   IDEA
@Project    :   Hanlp-Books-Examples
@File       :   DoubleArrayTrie.py
@Version    :   v0.1
@Time       :   2020-12-17 17:30
@License    :   (C)Copyright 2020-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
# 先引入 pyhanlp 激活 JVM 才能使用 jpype 调用 JClass
# import pyhanlp
# from jpype import JClass

# 通过 pyhanlp 间接调用 jpype.JClass 也完成了 JVM 的激活
from pyhanlp import JClass


class DoubleArrayTrie(object):
    def __init__(self, dat) -> None:
        self.base = dat.getBase()
        self.check = dat.getCheck()
        self.value = dat.getValueArray([''])

    @staticmethod
    def char_hash(c) -> int:
        return JClass('java.lang.Character')(c).hashCode()

    def transition(self, c, b) -> int:
        p = self.base[b] + self.char_hash(c) + 1
        if self.base[b] == self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self, key: str):
        b = 0
        for i in range(len(key)):
            p = self.transition(key[i], b)
            if p is not -1:
                b = p
            else:
                return None
        p = self.base[b]
        n = self.base[p]
        if p == self.check[p] and n < 0:
            index = -n - 1
            return self.value[index]
        return None


def main():
    dic = {
        "自然": 'nature',
        "自然人": 'human',
        "自然语言": 'language',
        "自语": 'talk to oneself',
        "入门": 'introduction'
    }
    m = JClass('java.util.TreeMap')()
    for k, v in dic.items():
        m[k] = v
    dat = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(m)
    tree = DoubleArrayTrie(dat)
    print(tree)
    assert tree["自然"] == 'nature'
    assert tree["自然语言"] == 'language'
    assert tree["不存在"] is None
    assert tree["自然\0在"] is None


if __name__ == '__main__':
    main()
