package ch01;


import com.hankcs.hanlp.HanLP;

public class HelloWorld {

    public static void main(String[] args) {
        System.out.print(HanLP.segment("你好，欢迎使用 Python 中调用 HanLP 的 API 接口！"));
        HanLP.Config.enableDebug();
        System.out.println(HanLP.segment("王国维和服务员"));
    }
}
