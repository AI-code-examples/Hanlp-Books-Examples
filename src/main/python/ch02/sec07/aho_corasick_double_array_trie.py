# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   aho_corasick_double_array_trie.py
@Version    :   v0.1
@Time       :   2020-12-19 10:24
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import JClass
from tools import beep_end


# ----------------------------------------------------------------------
def classic_demo():
    """
    使用 双数组字典树的 AC 自动机
    :return:
    """
    words = ['hers', 'his', 'she', 'he']
    map = JClass("java.util.TreeMap")()
    for word in words:
        map[word] = word.upper()
    trie = JClass("com.hankcs.hanlp.collection.AhoCorasick.AhoCorasickDoubleArrayTrie")(map)
    for hit in trie.parseText('ushers'):
        print("[%d:%d]=%s" % (hit.begin, hit.end, hit.value))


# ----------------------------------------------------------------------
def main():
    classic_demo()
    pass


if __name__ == '__main__':
    main()
    beep_end()