# Hanlp-Books-Examples

这个库是对《自然语言处理入门》书中的例子的修正，按照下文中指定的版本进行了测试。

-   [项目中的 Java 代码](https://github.com/zhuyuanxiang/Hanlp-Books-Examples/tree/main/src/main/java)
-   [项目中的 Python 代码](https://github.com/zhuyuanxiang/Hanlp-Books-Examples/tree/main/src/main/python)

如果需要原作者提供的例子可以参考下面的链接：

-   [原书中 Java 代码](https://github.com/hankcs/HanLP/tree/1.x/src/test/java/com/hankcs/book)
-   [原书中 Python 代码](https://github.com/hankcs/pyhanlp/tree/master/tests/book)

阅读总结：

这本书更像个自然语言处理的算法书。

## Environment

### java

[JDK下载](https://developers.redhat.com/products/openjdk/download?sc_cid=701f2000000RWTnAAO) ，建议下载 11.0的版本。

使用的开发包下载

-   JUnit5

### Python

Hanlp 1.x 的安装

1.  建议安装 Anaconda 5.x
2.  安装 pyhanlp

    ```powershell
    pip install pyhanlp
    conda install pyhamcrest
    conda install numpy
    ```

### IDE

主要工具：

-   Intelli IDEA Community Edition 2020.3
    -   Python Community PlugIn

辅助工具：

-   VSCode 1.52.0
    -   Python
    -   java

参考工具：

-   PyCharm Community Edition 2020.3

注：PyCharm、VSCode 与 IDEA 在配置文件的设置上会发生冲突，因此建议只使用 IDEA 进行学习。

## Support

下载支持文件：

-   开发包和源代码下载：[hanlp-1.7.8-release.zip](http://download.hanlp.com/hanlp-1.7.8-release.zip)
-   数据包下载：[data-for-1.7.5.zip](http://download.hanlp.com/data-for-1.7.5.zip)

注：使用 `hanlp` 命令时会自动下载支持的文件，如果无法正确下载，可以去上述地址下载。将两个文件解压到：`~\anaconda3\lib\site-packages\pyhanlp\static\`