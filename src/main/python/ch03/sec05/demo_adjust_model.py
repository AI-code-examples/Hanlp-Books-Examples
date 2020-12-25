# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_adjust_model.py
@Version    :   v0.1
@Time       :   2020-12-25 10:03
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import HanLP

from ch03.msr import msr_model
from ch03.sec03.demo_ngram_segment import load_bigram
from preamble import CoreDictionary
from tools import *


# ----------------------------------------------------------------------
def main():
    segment = load_bigram(model_path=msr_model, verbose=True, ret_viterbi=True)
    assert CoreDictionary.contains("管道")
    text = "北京输气管道工程"
    HanLP.Config.enableDebug()
    print(segment.seg(text))
    pass


if __name__ == '__main__':
    # Note: 运行后可能会影响到环境的编码设置，导致 Console 输出为乱码，重启一次环境就好了
    main()
    beep_end()
