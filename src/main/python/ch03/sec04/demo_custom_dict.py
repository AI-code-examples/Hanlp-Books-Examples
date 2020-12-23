# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_custom_dict.py
@Version    :   v0.1
@Time       :   2020-12-23 11:16
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   《自然语言处理入门》Sec3.4.5
@Desc       :   与用户词典的集成
@理解：
"""
from pyhanlp import CustomDictionary

from preamble import *
from tools import *


# ----------------------------------------------------------------------
def main():
    segment = ViterbiSegment()
    sentence = "社会摇摆简称社会摇"
    segment.enableCustomDictionary(False)
    print("不挂载词典：", segment.seg(sentence))
    CustomDictionary.insert("社会摇", "nz 100")
    segment.enableCustomDictionary(True)
    print("低优先级词典：", segment.seg(sentence))
    segment.enableCustomDictionary(True)
    print("高优先级词典：", segment.seg(sentence))
    pass


if __name__ == '__main__':
    main()
    beep_end()
