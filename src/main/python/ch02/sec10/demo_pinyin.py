# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_pinyin.py
@Version    :   v0.1
@Time       :   2020-12-20 12:33
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import *

from tools import beep_end


# ----------------------------------------------------------------------
def demo_pinyin():
    """ 汉字转拼音
    >>> demo_pinyin()
    原文： 重载不是重任！
    拼音（数字音调）： [chong2, zai3, bu2, shi4, zhong4, ren4, none5]
    拼音（符号音调）： chóng, zǎi, bú, shì, zhòng, rèn, none,
    拼音（无音调）： chong, zai, bu, shi, zhong, ren, none,
    声调： 2, 3, 2, 4, 4, 4, 5,
    声母： ch, z, b, sh, zh, r, none,
    韵母： ong, ai, u, i, ong, en, none,
    输入法头： ch, z, b, sh, zh, r, none,
    jie zhi none none none none nian none
    jie zhi 2 0 1 2 nian ，
    """
    Pinyin = JClass("com.hankcs.hanlp.dictionary.py.Pinyin")
    text = "重载不是重任！"
    pinyin_list = HanLP.convertToPinyinList(text)

    print("原文：", end=" ")
    print(text)

    print("拼音（数字音调）：", end=" ")
    print(pinyin_list)

    print("拼音（符号音调）：", end=" ")
    output = ""
    for pinyin in pinyin_list:
        output = output + ("%s, " % pinyin.getPinyinWithToneMark())
    print(output.strip(), end="")

    print("\n拼音（无音调）：", end=" ")
    output = ""
    for pinyin in pinyin_list:
        output = output + ("%s, " % pinyin.getPinyinWithoutTone())
    print(output.strip(), end="")

    print("\n声调：", end=" ")
    output = ""
    for pinyin in pinyin_list:
        output = output + ("%s, " % pinyin.getTone())
    print(output.strip(), end="")

    print("\n声母：", end=" ")
    output = ""
    for pinyin in pinyin_list:
        output = output + ("%s, " % pinyin.getShengmu())
    print(output.strip(), end="")

    print("\n韵母：", end=" ")
    output = ""
    for pinyin in pinyin_list:
        output = output + ("%s, " % pinyin.getYunmu())
    print(output.strip(), end="")

    print("\n输入法头：", end=" ")
    output = ""
    for pinyin in pinyin_list:
        output = output + ("%s, " % pinyin.getHead())
    print(output.strip(), end="")

    print()
    # 拼音转换可选保留无拼音的原字符
    print(HanLP.convertToPinyinString("截至2012年，", " ", True))
    print(HanLP.convertToPinyinString("截至2012年，", " ", False))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    beep_end()
