# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_corpus_loader.py
@Version    :   v0.1
@Time       :   2020-12-21 16:27
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   手工加载语料库
@理解：
"""
import os

from preamble import CorpusLoader
from tools import beep_end, test_data_path, show_title


def my_cws_corpus():
    corpus_path = test_data_path() + 'my_cws_corpus.txt'
    if not os.path.isfile(corpus_path):
        with open(corpus_path, 'w', encoding='utf-8') as out:
            out.write("商品 和 服务\n" + "商品 和服 物美价廉\n" + "服务 和 货币")
    return corpus_path


def load_cws_corpus(corpus_path):
    return CorpusLoader.convert2SentenceList(corpus_path)


# ----------------------------------------------------------------------
def main():
    corpus_path = my_cws_corpus()
    sents = load_cws_corpus(corpus_path)
    for sent in sents:
        show_title("")
        print("sent: ", sent)
        print("word: ", end='')
        for word in sent:
            print(word, end=', ')
        print()
    pass


if __name__ == '__main__':
    main()
    beep_end()
