package ch02.sec05;

import com.hankcs.hanlp.collection.trie.DoubleArrayTrie;
import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.io.IOException;
import java.util.TreeMap;

import static ch02.sec05.DoubleArrayTrieSegmentMethod.segmentForwardLongest;
import static ch02.sec05.DoubleArrayTrieSegmentMethod.segmentFully;

public class DoubleArrayTrieBasedSegmentation {
    public static void main(String[] args) throws IOException {
        testTinyDAT();
        testSpeed();
    }

    private static void testSpeed() throws IOException {
        // 加载词典
        TreeMap<String, CoreDictionary.Attribute> dictionary =
                IOUtil.loadDictionary("data/dictionary/CoreNatureDictionary.mini.txt");
        DoubleArrayTrie<CoreDictionary.Attribute> dat = new DoubleArrayTrie<CoreDictionary.Attribute>(dictionary);

        String text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原";
        long start;
        double costTime;
        final int pressure = 1000000;

        System.out.println("===DoubleArrayTrie接口===");
        System.out.println("完全切分");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            segmentFully(text, dat);
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f万字/秒\n", text.length() * pressure / 10000 / costTime);

        System.out.println("正向最长");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            segmentForwardLongest(text, dat);
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f万字/秒\n", text.length() * pressure / 10000 / costTime);
    }

    private static void testTinyDAT() {
        TreeMap<String, String> tinyDictionary = createTinyTreeMap();
        DoubleArrayTrie<String> dat = new DoubleArrayTrie<>(tinyDictionary);
        System.out.println(dat);
    }

    private static TreeMap<String, String> createTinyTreeMap() {
        TreeMap<String, String> tinyDictionary = new TreeMap<>();
        tinyDictionary.put("自然", "nature");
        tinyDictionary.put("自然人", "human");
        tinyDictionary.put("自然语言", "language");
        tinyDictionary.put("自语", "talk to oneself");
        tinyDictionary.put("入门", "introduction");
        return tinyDictionary;
    }
}
