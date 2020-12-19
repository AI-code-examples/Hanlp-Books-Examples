# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_dat_segment.py
@Version    :   v0.1
@Time       :   2020-12-19 11:04
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import HanLP, DoubleArrayTrieSegment

from tools import beep_end, show_title, get_root_path


# ----------------------------------------------------------------------
def main():
    HanLP.Config.ShowTermNature = False  # 关闭词性标注

    show_title("系统默认字典分词")
    segment = DoubleArrayTrieSegment()
    print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))

    show_title("自定义字典分词")
    root_path = get_root_path()
    dict1 = root_path + "/data/dictionary/CoreNatureDictionary.mini.txt"
    dict2 = root_path + "/data/dictionary/custom/上海地名.txt ns"
    segment = DoubleArrayTrieSegment([dict1, dict2])
    terms = segment.seg("上海市虹口区大连西路550号SISU")
    print(terms)

    show_title("自定义字典分词(增加英文识别)(增加词性说明)")
    segment.enablePartOfSpeechTagging(True)  # 激活数词和英文识别
    HanLP.Config.ShowTermNature = True  # 激活词性标注
    terms = segment.seg("上海市虹口区大连西路550号SISU")
    print(terms)

    for term in terms:
        print("单词：%s\t词性：%s" % (term.word, term.nature))


pass

if __name__ == '__main__':
    main()
    beep_end()
