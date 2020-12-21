# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   sighan05_statistics.py
@Version    :   v0.1
@Time       :   2020-12-20 17:41
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
import re
from collections import Counter

from tools import beep_end, get_root_path, show_title


# ----------------------------------------------------------------------
def count_word_freq(train_path: str):
    f = Counter()
    with open(train_path, encoding='utf-8') as src:
        for line in src:
            for word in re.compile("\\s+").split(line.strip()):
                f[word] += 1
    return f, sum(f.values()), sum(len(w) * f[w] for w in f.keys())


def count_corpus(train_path: str, test_path: str):
    train_counter, train_freq, train_chars = count_word_freq(train_path)
    test_counter, test_freq, test_chars = count_word_freq(test_path)
    test_oov = sum(test_counter[w] for w in (test_counter.keys() - train_counter.keys()))
    return (train_chars / 10000,
            len(train_counter) / 10000,
            train_freq / 10000,
            train_chars / train_freq,
            test_chars / 10000,
            len(test_counter) / 10000,
            test_freq / 10000,
            test_chars / test_freq,
            test_oov * 100 / test_freq)


def main():
    """
    语料库情况统计
    :return:
    """
    show_title("gold")
    print('|语料库|字符数|词语种数|总词频|平均词长|字符数|词语种数|总词频|平均词长|OOV|')
    icwb2_data_path = get_root_path() + "data/test/icwb2-data/gold/"
    for data in 'pku', 'msr', 'as', 'cityu':
        train_file = "{}_training_words.utf8".format(data)
        train_file_path = icwb2_data_path + train_file
        test_file = ('{}_testing_gold.utf8' if data == 'as' else '{}_test_gold.utf8').format(data)
        test_file_path = icwb2_data_path + test_file
        print('|%5s|%3.0f万|%4.0f万|%4.0f万|%7.1f|%3.0f万|%4.0f万|%4.0f万|%7.1f|%.2f%%|' %
              ((data.upper(),) + count_corpus(train_file_path, test_file_path)))

    show_title("training+testing")
    print('|语料库|字符数|词语种数|总词频|平均词长|字符数|词语种数|总词频|平均词长|OOV|')
    icwb2_data_path = get_root_path() + "data/test/icwb2-data/"
    for data in 'pku', 'msr', 'as', 'cityu':
        train_file = "training/{}_training.utf8".format(data)
        train_file_path = icwb2_data_path + train_file
        test_file = 'testing/{}_test.utf8'.format(data)
        test_file_path = icwb2_data_path + test_file
        print('|%5s|%3.0f万|%4.0f万|%4.0f万|%7.1f|%3.0f万|%4.0f万|%4.0f万|%7.1f|%.2f%%|' %
              ((data.upper(),) + count_corpus(train_file_path, test_file_path)))

    pass


if __name__ == '__main__':
    main()
    beep_end()
