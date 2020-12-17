# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   IDEA
@Project    :   Hanlp-Books-Examples
@File       :   NaiveDictionaryBasedSegmentation.py
@Version    :   v0.1
@Time       :   2020-12-16 17:41
@License    :   (C)Copyright 2020-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：虽然 Python 非常好用，但是因为原始的程序由 Java 编写，因此后面的扩展也建议用 Java，方便利用 Java 的特性避免程序错误
"""
from time import time

from pyhanlp import JClass
from pyhanlp import HanLP

from tools import show_subtitle


def load_dictionary():
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())


def fully_segment(text, dic):
    """
    完全切分式的中文分词算法
    :param text: 待分词的文本
    :param dic: 词典
    :return: 单词列表
    """
    word_list = []
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word in dic:
                word_list.append(word)
    return word_list


def forward_segment(text, dic):
    """
    正向最长匹配的中文分词算法
    :param text:待分词的文本
    :param dic:词典
    :return:单词列表
    """
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
        word_list.append(longest_word)  # 正向搜索，越先找到的单词排在越前面
        i += len(longest_word)
    return word_list


def backward_segment(text, dic):
    word_list = []
    i = len(text) - 1
    while i >= 0:
        longest_word = text[i:i + 1]
        for j in range(i):
            word = text[j:i + 1]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
                    break
        word_list.insert(0, longest_word)  # 逆向搜索，越后找到的单词排在越前面
        i -= len(longest_word)
    return word_list


def count_single_char(word_list: list):
    return sum(1 for word in word_list if len(word) == 1)


def bidirectional_segment(text, dic):
    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    # 分割的单词越少的优先级越高
    if len(f) < len(b):
        return f
    elif len(f) > len(b):
        return b
    else:
        # 分割的单词数量一样时，单字越少的优先级越高
        if count_single_char(f) < count_single_char(b):
            return f
        else:
            return b


def evaluate_speed(desc, segment, text, dic):
    start_time = time()
    PRESSURE = 10000
    show_subtitle(desc)
    for i in range(PRESSURE):
        segment(text, dic)
    elapsed_time = time() - start_time
    print("%.2f 万字/秒\n" % (len(text) * PRESSURE / 10000 / elapsed_time))


def main():
    dictionary = load_dictionary()
    print("词典大小：{}个词条".format(len(dictionary)))
    print("词典内容：", list(dictionary)[0:10])
    show_subtitle("完全切分")
    print(fully_segment("就读北京大学", dictionary))
    show_subtitle("正向最长匹配")
    print(forward_segment("就读北京大学", dictionary))
    print(forward_segment("研究生命起源", dictionary))
    print(forward_segment("项目的研究", dictionary))
    show_subtitle("逆向最长匹配")
    print(backward_segment("就读北京大学", dictionary))
    print(backward_segment("研究生命起源", dictionary))
    show_subtitle("|文本编号|文本内容|正向最长匹配|逆向最长匹配|双向最长匹配|")
    document = [
        "项目的研究",
        "商品和服务",
        "研究生命起源",
        "当下雨天地面积水",
        "结婚的和尚未结婚的",
        "欢迎新老师生前来就餐",
    ]
    for i, sentence in enumerate(document):
        print(
            "| %d | %s | %s | %s | %s|\n" %
            (i + 1,
             sentence,
             forward_segment(sentence, dictionary),
             backward_segment(sentence, dictionary),
             bidirectional_segment(sentence, dictionary),
             )
        )
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    evaluate_speed("正向最长", forward_segment, text, dictionary)
    evaluate_speed("逆向最长", backward_segment, text, dictionary)
    evaluate_speed("双向最长", bidirectional_segment, text, dictionary)


if __name__ == '__main__':
    main()
