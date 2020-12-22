# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   demo_ngram_segment.py
@Version    :   v0.1
@Time       :   2020-12-22 9:53
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
import os

from pyhanlp import HanLP

from ch03.sec03.demo_corpus_loader import my_cws_corpus
from preamble import *
from tools import beep_end, test_data_path


# ----------------------------------------------------------------------
def train_bigram(corpus_path, model_path):
    sents = CorpusLoader.convert2SentenceList(corpus_path)
    for sent in sents:
        for word in sent:
            if word.label is None:
                word.setLabel("n")
    marker = NatureDictionaryMaker()
    marker.compute(sents)
    marker.saveTxtTo(model_path)
    pass


def generate_wordnet(sent, trie):
    searcher = trie.getSearcher(JString(sent), 0)
    wordnet = WordNet(sent)
    while searcher.next():
        idx = searcher.begin + 1
        vertex = Vertex(sent[searcher.begin:searcher.begin + searcher.length], searcher.value, searcher.index)
        wordnet.add(idx, vertex)
    # 原子分词，保证图连通
    vertexes = wordnet.getVertexes()
    i = 0
    while i < len(vertexes):
        if len(vertexes[i]) == 0:
            j = i + 1
            for j in range(i + 1, len(vertexes) - 1):  # 寻找第一个非空行 j
                if len(vertexes[j]):
                    break
            vertex = Vertex.newPunctuationInstance(sent[i - 1:j - 1])
            wordnet.add(i, vertex)  # 填充 [i,j) 之间的空白行
            i = j
        else:
            i += len(vertexes[i][-1].realWord)
    return wordnet


def viterbi(wordnet):
    nodes = wordnet.getVertexes()
    # 前向遍历
    for i in range(len(nodes) - 1):
        for node in nodes[i]:
            for to in nodes[i + len(node.realWord)]:
                to.updateFrom(node)  # 根据距离公式计算节点距离，并维护最短路径上的前驱指针from

    # 后向回溯
    path = []  # 最短路径
    f = nodes[len(nodes) - 1].getFirst()  # 从终点回溯
    while f:
        path.insert(0, f)
        f = f.getFrom()  # 按前驱指针 from 回溯
    return [v.realWord for v in path]


def load_bigram(model_path, verbose=True, ret_viterbi=True):
    HanLP.Config.CoreDictionaryPath = model_path + ".txt"
    HanLP.Config.BiGramDictionaryPath = model_path + ".ngram.txt"
    if verbose:
        print(CoreDictionary.getTermFrequency("商品"))
        print(CoreBiGramTableDictionary.getBiFrequency("商品", "和"))
        sent = "商品和服务"
        wordnet = generate_wordnet(sent, CoreDictionary.trie)
        print(wordnet)
        print(viterbi(wordnet))
    viterb_segment = ViterbiSegment().enableAllNamedEntityRecognize(False).enableCustomDictionary(False)
    dijkstra_segment = DijkstraSegment().enableAllNamedEntityRecognize(False).enableCustomDictionary(False)
    return viterb_segment if ret_viterbi else dijkstra_segment


def main():
    corpus_path = my_cws_corpus()
    model_path = os.path.join(test_data_path(), 'my_cws_model')
    train_bigram(corpus_path, model_path)
    load_bigram(model_path)
    pass


if __name__ == '__main__':
    main()
    beep_end()
