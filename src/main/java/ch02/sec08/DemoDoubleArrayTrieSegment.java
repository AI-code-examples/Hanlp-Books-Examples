package ch02.sec08;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.seg.Other.DoubleArrayTrieSegment;
import com.hankcs.hanlp.seg.common.Term;
import tools.Tools;

import java.io.IOException;
import java.util.List;

public class DemoDoubleArrayTrieSegment {
    public static void main(String[] args) throws IOException {
        HanLP.Config.ShowTermNature = false;  // 关闭词性标注

        // 默认加载配置文件中 CoreDictionaryPath 指定的字典
        Tools.show_subtitle("系统默认字典分词");
        DoubleArrayTrieSegment segment = new DoubleArrayTrieSegment();
        System.out.println(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"));

        // 加载多个自定义字典
        Tools.show_subtitle("自定义字典分词");
        String dict1 = "data/dictionary/CoreNatureDictionary.mini.txt";
        String dict2 = "data/dictionary/custom/上海地名.txt ns";
        segment = new DoubleArrayTrieSegment(dict1, dict2);
        List<Term> terms = segment.seg("上海市虹口区大连西路550号SISU");
        System.out.println(terms);

        Tools.show_subtitle("自定义字典分词(增加英文识别)(增加词性说明)");
        segment.enablePartOfSpeechTagging(true);    // 激活数词和英文识别
        HanLP.Config.ShowTermNature = true;// 激活词性标注
        terms = segment.seg("上海市虹口区大连西路550号SISU");
        System.out.println(terms);

        for (Term term : terms)
            System.out.printf("单词：%s\t词性：%s\n", term.word, term.nature);
    }
}
