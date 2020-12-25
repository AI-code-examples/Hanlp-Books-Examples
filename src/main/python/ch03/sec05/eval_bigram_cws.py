# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   eval_bigram_cws.py
@Version    :   v0.1
@Time       :   2020-12-23 11:26
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   《自然语言处理入门》 3.5 评测
@Desc       :   二元语法训练模型
@理解：
"""
from ch03.msr import msr_dict
from ch03.msr import msr_gold
from ch03.msr import msr_model
from ch03.msr import msr_output
from ch03.msr import msr_test
from ch03.msr import msr_train
from ch03.sec03.demo_ngram_segment import load_bigram
from ch03.sec03.demo_ngram_segment import train_bigram
from preamble import CWSEvaluator


# ----------------------------------------------------------------------
from tools import beep_end


def main():
    train_bigram(msr_train, msr_model)
    segment = load_bigram(msr_model)
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)
    print(result)
    pass


if __name__ == '__main__':
    main()
    beep_end()
