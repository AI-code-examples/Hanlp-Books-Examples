# -*- encoding: utf-8 -*-    
"""
@Author     :   zYx.Tom
@Contact    :   526614962@qq.com
@site       :   https://zhuyuanxiang.github.io
---------------------------
@Software   :   IDEA
@Project    :   Hanlp-Books-Examples
@File       :   tools.py
@Version    :   v0.1
@Time       :   2020-12-16 17:57
@License    :   (C)Copyright 2020-2020, zYx.Tom
@Reference  :   
@Desc       :   
@理解：
"""
import os


def show_subtitle(message):
    # 输出运行模块的子标题
    print('-' * 15, '>' + message + '<', '-' * 15)
    pass


def show_title(message):
    # 输出运行模块的子标题
    print()
    print('=' * 15, '>' + message + '<', '=' * 15)
    pass


def beep_end():
    # 运行结束的提醒
    import winsound
    winsound.Beep(600, 500)
    pass


def get_root_path():
    import os
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = cur_path[:cur_path.find("Hanlp-Books-Examples\\") + len("Hanlp-Books-Examples\\")]
    return root_path


def test_data_path():
    """
    获取测试数据路径，位于$root/data/test，根目录 $root 由配置文件 hanlp.properties 指定。
    :return: 测试数据路径
    """
    data_path = os.path.join(get_root_path(), 'data/test/')
    if not os.path.isdir(data_path):
        os.mkdir(data_path)
    return data_path
