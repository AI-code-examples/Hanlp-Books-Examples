/*
 * <summary></summary>
 * <author>zYx.Tom</author>
 * <email>zhuyuanxiang@gmail.com</email>
 * <create-date>2020-12-23 11:02</create-date>
 */
package ch03.sec04;

import com.hankcs.hanlp.dictionary.CustomDictionary;
import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.Viterbi.ViterbiSegment;

/**
 * 《自然语言处理入门》 3.4.5 与用户词典的集成
 */
public class DemoCustomDictionary {
    public static void main(String[] args) {
        Segment segment = new ViterbiSegment();
        final String sentence = "社会摇摆简称社会摇";
        segment.enableCustomDictionary(false);
        System.out.println("不挂载词典：" + segment.seg(sentence));
        CustomDictionary.insert("社会摇", "nz 100");
        segment.enableCustomDictionary(true);
        System.out.println("低优先级词典：" + segment.seg(sentence));
        segment.enableCustomDictionaryForcing(true);
        System.out.println("高优先级词典：" + segment.seg(sentence));
    }
}
