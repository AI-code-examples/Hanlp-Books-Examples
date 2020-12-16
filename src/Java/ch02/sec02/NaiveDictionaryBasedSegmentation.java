package Java.ch02.sec02;

import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;

public class NaiveDictionaryBasedSegmentation {
    public static void main(String[] args) throws IOException {
        // 加载词典
        TreeMap<String, CoreDictionary.Attribute> dictionary =
                IOUtil.loadDictionary("data/dictionary/CoreNatureDictionary.mini.txt");
        System.out.printf("词典大小：%d个词条\n", dictionary.size());
        System.out.println(dictionary.keySet().iterator().next());

        // 完全切分
        System.out.println(SegmentMethod.segmentFully("就读北京大学", dictionary));
        // 正向最长匹配
        System.out.println(SegmentMethod.segmentForwardLongest("就读北京大学", dictionary));
        System.out.println(SegmentMethod.segmentForwardLongest("研究生命起源", dictionary));
        System.out.println(SegmentMethod.segmentForwardLongest("项目的研究", dictionary));
        // 逆向最长匹配
        System.out.println(SegmentMethod.segmentBackwardLongest("就读北京大学", dictionary));
        System.out.println(SegmentMethod.segmentBackwardLongest("研究生命起源", dictionary));
        // 双向最长匹配
        String[] text = new String[]{
                "项目的研究",
                "商品和服务",
                "研究生命起源",
                "当下雨天地面积水",
                "结婚的和尚未结婚的",
                "欢迎新老师生前来就餐",
        };
        for (int i = 0; i < text.length; i++) {
            System.out.printf("| %d | %s | %s | %s | %s|\n",
                    i + 1,
                    text[i],
                    SegmentMethod.segmentForwardLongest(text[i], dictionary),
                    SegmentMethod.segmentBackwardLongest(text[i], dictionary),
                    SegmentMethod.segmentBidirectional(text[i], dictionary)
            );
        }

        evaluateSpeed(dictionary);
    }

    /**
     * 评测速度
     *
     * @param dictionary 词典
     */
    public static void evaluateSpeed(Map<String, CoreDictionary.Attribute> dictionary) {
        String text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原";
        long start;
        double costTime;
        final int pressure = 10000;

        System.out.println("正向最长");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            SegmentMethod.segmentForwardLongest(text, dictionary);

        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f万字/秒\n", text.length() * pressure / 10000 / costTime);

        System.out.println("逆向最长");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            SegmentMethod.segmentBackwardLongest(text, dictionary);

        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f万字/秒\n", text.length() * pressure / 10000 / costTime);

        System.out.println("双向最长");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            SegmentMethod.segmentBidirectional(text, dictionary);

        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f万字/秒\n", text.length() * pressure / 10000 / costTime);


    }
}
