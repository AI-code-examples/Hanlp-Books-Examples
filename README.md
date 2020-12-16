# Hanlp-Books-Examples

《自然语言处理入门》书中的例子

## Environment

### java

[JDK下载](https://developers.redhat.com/products/openjdk/download?sc_cid=701f2000000RWTnAAO)，建议下载 11.0的版本。

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

注：PyCharm 与 IDEA 在配置文件的设置上会发生冲突，因此建议主要使用 IDEA 进行学习，使用 VSCode 补充其不足的功能。

## Support

下载支持文件：

[hanlp-1.7.8-release.zip](http://download.hanlp.com/hanlp-1.7.8-release.zip)

[data-for-1.7.5.zip](http://download.hanlp.com/data-for-1.7.5.zip)

将两个文件解压到：`~\anaconda3\lib\site-packages\pyhanlp\static\`

注：使用 `hanlp` 命令时会自动下载支持的文件，如果无法正确下载，可以去上述地址下载。