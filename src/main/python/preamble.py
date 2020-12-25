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
from pyhanlp import JClass
from pyhanlp import LazyLoadingJClass
from pyhanlp import SafeJClass

from tools import beep_end

CoreBiGramTableDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CoreBiGramTableDictionary')
CoreDictionary = LazyLoadingJClass('com.hankcs.hanlp.dictionary.CoreDictionary')
CorpusLoader = SafeJClass('com.hankcs.hanlp.corpus.document.CorpusLoader')
CWSEvaluator = SafeJClass('com.hankcs.hanlp.seg.common.CWSEvaluator')
DijkstraSegment = JClass('com.hankcs.hanlp.seg.Dijkstra.DijkstraSegment')
JString = JClass('java.lang.String')
Nature = JClass('com.hankcs.hanlp.corpus.tag.Nature')
NatureDictionaryMaker = SafeJClass('com.hankcs.hanlp.corpus.dictionary.NatureDictionaryMaker')
Vertex = JClass('com.hankcs.hanlp.seg.common.Vertex')
ViterbiSegment = JClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')
WordNet = JClass('com.hankcs.hanlp.seg.common.WordNet')
FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
HMMSegmenter = JClass('com.hankcs.hanlp.model.hmm.HMMSegmenter')


# ----------------------------------------------------------------------
def main():
    pass


if __name__ == '__main__':
    main()
    beep_end()
