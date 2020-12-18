package ch02.sec06;

import static ch02.sec06.AhoCorasickSegmentMethod.segmentFully;

import java.io.IOException;
import java.util.TreeMap;

import com.hankcs.hanlp.algorithm.ahocorasick.trie.Emit;
import com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie;
import com.hankcs.hanlp.dictionary.CoreDictionary;
import data.Dictionary;

public class AhoCorasickSegmentation {
    public static void main(String[] args) throws IOException {
        classicDemo();
        evaluateSpeed();
    }

    private static void evaluateSpeed() throws IOException {
        // 加载词典
        TreeMap<String, CoreDictionary.Attribute> dictionary = Dictionary.loadDictionary(-1);
        Trie trie = new Trie(dictionary.keySet());

        String text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原";
        long start;
        double costTime;
        final int pressure = 1000000;

        System.out.println("===AC自动机接口===");
        System.out.println("完全切分");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
        {
            segmentFully(text, trie);
        }
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f 万字/秒\n", text.length() * pressure / 10000 / costTime);
    }

    private static void classicDemo() {
        String[] keyArray=new String[]{"hers","his","she","he"};
        Trie trie=new Trie();
        for(String key:keyArray)
            trie.addKeyword(key);
        for(Emit emit: trie.parseText("ushers"))
            System.out.printf("[%d:%d]=%s\n",emit.getStart(),emit.getEnd(),emit.getKeyword());

    }
}
