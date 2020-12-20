# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_stopwords.py
@Version    :   v0.1
@Time       :   2020-12-20 12:06
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from jpype import JString
from pyhanlp import JClass, HanLP, DoubleArrayTrieSegment

from tools import beep_end


# ----------------------------------------------------------------------
def load_from_file(path):
    map = JClass("java.util.TreeMap")()
    with open(path, encoding='utf-8') as src:
        for word in src:
            word = word.strip()  # 去掉Python读入时的\n
            map[word] = word
    return JClass("com.hankcs.hanlp.collection.trie.DoubleArrayTrie")(map)


def remove_stopwords_termlist(termlist, trie):
    return [term.word for term in termlist if not trie.containsKey(term.word)]


def load_from_words(*words):
    map = JClass("java.util.TreeMap")()
    for word in words:
        map[word] = word
    return JClass("com.hankcs.hanlp.collection.trie.DoubleArrayTrie")(map)


def replace_stopwords_text(text, replacement, trie):
    searcher = trie.getLongestSearcher(JString(text), 0)
    offset = 0
    result = ''
    while searcher.next():
        begin = searcher.begin
        end = begin + searcher.length
        if begin > offset:
            result += text[offset:begin]
        result += replacement
        offset = end
    if offset < len(text):
        result += text[offset:]
    return result


def main():
    HanLP.Config.ShowTermNature = False
    trie = load_from_file(HanLP.Config.CoreStopWordDictionaryPath)
    text = "停用词的意义相对而言无关紧要吧。"
    segment = DoubleArrayTrieSegment()
    termlist = segment.seg(text)
    print("分词结果：", termlist)
    print("分词结果去除停用词：", remove_stopwords_termlist(termlist, trie))
    trie = load_from_words("的", "相对而言", "吧")
    print("不分词去掉停用词：", replace_stopwords_text(text, "**", trie))

    pass


if __name__ == '__main__':
    main()
    beep_end()
