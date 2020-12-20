package ch02.sec10;

import com.hankcs.hanlp.HanLP;

public class DemoTraditionalChinese2SimplifiedChinese {
    public static void main(String[] args) {
        System.out.println(HanLP.convertToTraditionalChinese("“以后等你当上皇后，就能买草莓庆祝了”。发现一根白头发"));
        System.out.println(HanLP.convertToSimplifiedChinese("憑藉筆記簿型電腦寫程式HanLP"));
        // 简体转台湾繁体
        System.out.println(HanLP.s2tw("hankcs在台湾写代码"));
        // 台湾繁体转简体
        System.out.println(HanLP.tw2s("hankcs在臺灣寫程式碼"));
        // 简体转香港繁体
        System.out.println(HanLP.s2hk("hankcs在香港写代码"));
        // 香港繁体转简体
        System.out.println(HanLP.hk2s("hankcs在香港寫代碼"));
        // 香港繁体转台湾繁体
        System.out.println(HanLP.hk2tw("hankcs在臺灣寫代碼"));
        // 台湾繁体转香港繁体
        System.out.println(HanLP.tw2hk("hankcs在香港寫程式碼"));

        // 香港/台湾繁体和HanLP标准繁体的互转
        System.out.println(HanLP.t2tw("hankcs在臺灣寫代碼"));
        System.out.println(HanLP.t2hk("hankcs在臺灣寫代碼"));

        System.out.println(HanLP.tw2t("hankcs在臺灣寫程式碼"));
        System.out.println(HanLP.hk2t("hankcs在台灣寫代碼"));
    }
}
