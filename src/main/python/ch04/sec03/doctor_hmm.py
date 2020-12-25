# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   PyCharm
@Project    :   Hanlp-Books-Examples
@File       :   doctor_hmm.py
@Version    :   v0.1
@Time       :   2020-12-25 10:43
@License    :   (C)Copyright 2018-2020, zYx.Tom
@Reference  :   《自然语言处理入门》
@Desc       :   4.3 隐马尔可夫模型案例——医疗诊断
@理解：
"""
import numpy as np
from jpype import JArray
from jpype import JFloat
from jpype import JInt

from preamble import *
from tools import *


# ----------------------------------------------------------------------
def generate_index_map(labels):
    # 生成两个字典
    label_index = {}  # 编号到索引字典
    index_label = {}  # 索引到编号字典
    # i=0
    for i, l in enumerate(labels):
        label_index[l] = i
        index_label[i] = l
    return label_index, index_label
    pass


def convert_map_to_matrix(label_map, label_index1, label_index2):
    m = np.empty((len(label_index1), len(label_index2)), dtype=float)
    for line in label_map:
        for col in label_map[line]:
            m[label_index1[line]][label_index2[col]] = label_map[line][col] = label_map[line][col]
    return JArray(JFloat, m.ndim)(m.tolist())


def convert_observations_to_index(observations, label_index):
    # list=[]
    # for o in observations:
    #     list.append(label_index[o])
    # return list
    return [label_index[o] for o in observations]


def convert_map_to_vector(label_map, label_index):
    v = np.empty(len(label_map), dtype=float)
    for e in label_map:
        v[label_index[e]] = label_map[e]
    return JArray(JFloat, v.ndim)(v.tolist())


def main():
    states = ('Healthy', 'Fever')
    start_probability = {'Healthy': 0.6, 'Fever': 0.4}
    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6}
    }
    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
    }
    observations = {'normal', 'cold', 'dizzy'}
    states_label_index, states_index_label = generate_index_map(states)
    observations_label_index, observations_index_label = generate_index_map(observations)
    A = convert_map_to_matrix(transition_probability, states_label_index, states_label_index)
    B = convert_map_to_matrix(emission_probability, states_label_index, observations_label_index)
    observations_index = convert_observations_to_index(observations, observations_label_index)
    pi = convert_map_to_vector(start_probability, states_label_index)
    given_model = FirstOrderHiddenMarkovModel(pi, A, B)
    for O, S in given_model.generate(3, 5, 2):
        print(" ".join((observations_index_label[o] + '/' + states_index_label[s]) for o, s in zip(O, S)))

    trained_model = FirstOrderHiddenMarkovModel()
    trained_model.train(given_model.generate(3, 10, 100000))
    assert trained_model.similar(given_model)
    trained_model.unLog()  # 还原对数形式的概率
    print(trained_model.start_probability)
    for vec in trained_model.transition_probability:
        print(vec)
    for vec in trained_model.emission_probability:
        print(vec)

    pred = JArray(JInt, 1)([0, 0, 0])
    prob = given_model.predict(observations_index, pred)
    print(" ".join((observations_index_label[o] + '/' + states_index_label[s]) for o, s in
                   zip(observations_index, pred)) + " {:.3f}".format(np.math.exp(prob)))
    pass


if __name__ == '__main__':
    main()
    beep_end()
