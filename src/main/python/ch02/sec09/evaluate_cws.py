# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   evaluate_cws.py
@Version    :   v0.1
@Time       :   2020-12-19 12:04
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
import re

from pyhanlp import JClass

from tools import beep_end, get_root_path


# ----------------------------------------------------------------------
def to_region(segmentation: str) -> list:
    """
    将分词结果转换为区间
    :param segmentation:商品 和 服务
    :return:[(0,2),(2,3),(3,5)]
    """
    region = []
    start = 0
    for word in re.compile("\\s+").split(segmentation.strip()):
        end = start + len(word)
        region.append((start, end))
        start = end
    return region


def prf(gold: str, pred: str, dic) -> tuple:
    """
    计算 P、R、F1
    :param gold: 标准答案文件，内容是「商品 和 服务」
    :param pred: 分词结果文件，内容是「商品 和服 务」
    :param dic: 词典
    :return: (P、R、F1、OOV_R、IV_R)
    """
    A_size, B_size, A_cap_B_size, OOV, IV, OOV_R, IV_R = 0, 0, 0, 0, 0, 0, 0
    with open(gold, encoding='utf-8') as gd, open(pred, encoding='utf-8') as pd:
        for g, p in zip(gd, pd):
            A, B = set(to_region(g)), set(to_region(p))
            A_size += len(A)
            B_size += len(B)
            A_cap_B_size += len(A & B)
            text = re.sub("\\s+", "", g)
            for (start, end) in A:
                word = text[start:end]
                if dic.containsKey(word):
                    IV += 1
                else:
                    OOV += 1

            for (start, end) in A & B:
                word = text[start:end]
                if dic.containsKey(word):
                    IV_R += 1
                else:
                    OOV_R += 1

    p, r = A_cap_B_size * 100 / B_size, A_cap_B_size * 100 / A_size
    return p, r, 2 * p * r / (p + r), OOV_R * 100 / OOV, IV_R * 100 / IV


def main():
    print(to_region("商品 和 服务"))

    # icwb2-data.zip 的下载地址：http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip
    # 也可以访问链接：https://pan.baidu.com/s/1rDpWeknm13dyoyjsqu7zFg 提取码：eq5x
    # 或者这里：https://github.com/yuikns/icwb2-data
    # 项目中也已经提供了相应的数据文件

    root_path = get_root_path()
    msr_dict = root_path + "/data/test/icwb2-data/gold/msr_training_words.utf8"
    msr_test = root_path + "/data/test/icwb2-data/testing/msr_test.utf8"
    msr_output = root_path + "/data/test/icwb2-data/testing/msr_output.txt"
    msr_gold = root_path + "/data/test/icwb2-data/gold/msr_test_gold.utf8"

    DoubleArrayTrieSegment = JClass("com.hankcs.hanlp.seg.Other.DoubleArrayTrieSegment")
    segment = DoubleArrayTrieSegment([msr_dict]).enablePartOfSpeechTagging(True)
    with open(msr_gold, encoding='utf-8') as test, open(msr_output, 'w', encoding='utf-8') as output:
        for line in test:
            output.write(" ".join(term.word for term in segment.seg(re.sub("\\s+", "", line))))
            output.write('\n')
    print("P:%.2f R:%.2f F1:%.2f OOV-R:%.2f IV-R:%.2f" % prf(msr_gold, msr_output, segment.trie))
    pass


if __name__ == '__main__':
    main()
    beep_end()
