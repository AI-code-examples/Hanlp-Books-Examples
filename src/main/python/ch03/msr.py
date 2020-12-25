# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   msr.py
@Version    :   v0.1
@Time       :   2020-12-23 11:44
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :
@Desc       :
@理解：
"""
from tools import icwb2_data_path
from tools import test_data_path

msr_dict = icwb2_data_path() + "gold/msr_training_words.utf8"
msr_gold = icwb2_data_path() + "gold/msr_test_gold.utf8"
msr_model = test_data_path() + "msr_cws"
msr_output = icwb2_data_path() + "testing/msr_output.txt"
msr_test = icwb2_data_path() + "testing/msr_test.utf8"
msr_train = icwb2_data_path() + "training/msr_training.utf8"
