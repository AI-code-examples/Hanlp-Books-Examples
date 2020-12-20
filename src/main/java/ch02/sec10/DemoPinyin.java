package ch02.sec10;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.dictionary.py.Pinyin;
import tools.Tools;

import java.util.List;

public class DemoPinyin {
    public static void main(String[] args) {
        String text = "重载不是重任！";
        List<Pinyin> pinyinList = HanLP.convertToPinyinList(text);
        System.out.print("原文：");
        for (char c : text.toCharArray())
            System.out.printf("%c,", c);
        System.out.println();

        System.out.print("拼音（数字音调）：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin);
        System.out.println();

        System.out.print("拼音（符号音调）：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin.getPinyinWithToneMark());
        System.out.println();

        System.out.print("拼音（无音调）：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin.getPinyinWithoutTone());
        System.out.println();

        System.out.print("声调：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin.getTone());
        System.out.println();

        System.out.print("声母：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin.getShengmu());
        System.out.println();

        System.out.print("韵母：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin.getYunmu());
        System.out.println();

        System.out.print("输入法头：");
        for (Pinyin pinyin : pinyinList)
            System.out.printf("%s,", pinyin.getHead());
        System.out.println();

        Tools.show_title("拼音转换可选保留无拼音的原字符");

        text = "截至2012年，";
        System.out.println("原文：" + text);
        System.out.println("字符转换成拼音："+HanLP.convertToPinyinString(text, ",", true));
        System.out.println("字符不转换成拼音："+HanLP.convertToPinyinString(text, ",", false));
    }
}
