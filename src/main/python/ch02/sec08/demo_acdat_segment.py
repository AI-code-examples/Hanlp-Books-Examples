# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_acdat_segment.py
@Version    :   v0.1
@Time       :   2020-12-19 11:35
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import HanLP, JClass

from tools import beep_end


# ----------------------------------------------------------------------
def main():
    HanLP.Config.ShowTermNature = False
    segment = JClass("com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment")(HanLP.Config.CoreDictionaryPath)
    print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))
    pass


if __name__ == '__main__':
    main()
    beep_end()
