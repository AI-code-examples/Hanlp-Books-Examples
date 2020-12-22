# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   preamble.py
@Version    :   v0.1
@Time       :   2020-12-21 16:28
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
from pyhanlp import SafeJClass, JClass, LazyLoadingJClass

from tools import beep_end

NatureDictionaryMaker = SafeJClass('com.hankcs.hanlp.corpus.dictionary.NatureDictionaryMaker')
CorpusLoader = SafeJClass('com.hankcs.hanlp.corpus.document.CorpusLoader')
WordNet = JClass('com.hankcs.hanlp.seg.common.WordNet')
Vertex = JClass('com.hankcs.hanlp.seg.common.Vertex')
ViterbiSegment = JClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')
DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')
CoreDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CoreDictionary')
CoreBiGramTableDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CoreBiGramTableDictionary')
Nature = JClass('com.hankcs.hanlp.corpus.tag.Nature')
JString=JClass('java.lang.String')


# ----------------------------------------------------------------------
def main():
    pass


if __name__ == '__main__':
    main()
    beep_end()
