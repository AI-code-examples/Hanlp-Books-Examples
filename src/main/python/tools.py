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
