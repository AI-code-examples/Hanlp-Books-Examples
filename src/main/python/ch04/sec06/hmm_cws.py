# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   hmm_cws.py
@Version    :   v0.1
@Time       :   2020-12-25 15:12
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   《自然语言处理入门》
@Desc       :   
@理解：
"""

from ch03.msr import msr_dict
from ch03.msr import msr_gold
from ch03.msr import msr_output
from ch03.msr import msr_test
from ch03.msr import msr_train
from preamble import *
from tools import *


# ----------------------------------------------------------------------
def train(corpus, model):
    segmenter = HMMSegmenter(model)
    segmenter.train(corpus)
    print(segmenter.segment("商品和服务"))
    return segmenter.toSegment()


def evaluate(segment):
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)
    print(result)
    pass


def main():
    segment = train(msr_train, FirstOrderHiddenMarkovModel())
    evaluate(segment)
    segment = train(msr_train, SecondOrderHiddenMarkovModel())
    evaluate(segment)
    pass


if __name__ == '__main__':
    main()
    beep_end()
