package ch02.sec07;

import com.hankcs.hanlp.collection.AhoCorasick.AhoCorasickDoubleArrayTrie;
import com.hankcs.hanlp.collection.trie.DoubleArrayTrie;
import com.hankcs.hanlp.dictionary.CoreDictionary;
import data.Dictionary;

import java.io.IOException;
import java.util.TreeMap;

public class AhoCorasickDoubleArrayTrieSegmentation {
    public static void main(String[] args) throws IOException {
        classicDemo();
        for (int i = 1; i <= 10; ++i) {
            evaluateSpeed(i);
            System.gc();

        }
    }

    private static void evaluateSpeed(int wordLength) throws IOException {
        TreeMap<String, CoreDictionary.Attribute> dictionary = Dictionary.loadDictionary(wordLength);
        AhoCorasickDoubleArrayTrie<CoreDictionary.Attribute> acdat = new AhoCorasickDoubleArrayTrie<>(dictionary);
        DoubleArrayTrie<CoreDictionary.Attribute> dat = new DoubleArrayTrie<>(dictionary);

        String text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原";
        long start;
        double costTime;
        final int pressure = 1000000;
        System.out.printf("长度%d：\n", wordLength);

        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            acdat.parseText(text, (begin, end, value) -> {
            });
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("ACDAT: %.2f万字/秒\n", text.length() * pressure / 10000 / costTime);

        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            dat.parseText(text, ((begin, end, value) -> {
            }));
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("DAT: %.2f万字/秒\n", text.length() * pressure / 10000 / costTime);
    }

    private static void classicDemo() {
        String[] keyArray = new String[]{"hers", "his", "she", "he"};
        TreeMap<String, String> map = new TreeMap<>();
        for (String key : keyArray)
            map.put(key, key.toUpperCase());
        AhoCorasickDoubleArrayTrie<String> acdat = new AhoCorasickDoubleArrayTrie<>(map);
        for (AhoCorasickDoubleArrayTrie<String>.Hit<String> hit : acdat.parseText("ushers"))// 一下子获取全部结果
            System.out.printf("[%d:%d]=%s\n", hit.begin, hit.end, hit.value);
        System.out.println();
        acdat.parseText("ushers", (begin, end, value) -> System.out.printf("[%d:%d]=%s\n", begin, end, value));
    }
}
