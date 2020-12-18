# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   IDEA
@Project    :   Hanlp-Books-Examples
@File       :   aho_corasick.py
@Version    :   v0.1
@Time       :   2020-12-18 10:32
@License    :   (C)Copyright 2020-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import JClass


def classic_demo():
    words = ['hers', 'his', 'she', 'he']
    Trie = JClass("com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie")
    trie = Trie()
    for w in words:
        trie.addKeyword(w)

    for emit in trie.parseText("ushers"):
        print("[%d:%d]=%s\n" % (emit.getStart(), emit.getEnd(), emit.getKeyword()))


if __name__ == '__main__':
    classic_demo()
