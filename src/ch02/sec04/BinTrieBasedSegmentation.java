package ch02.sec04;

import ch02.sec02.NaiveSegmentMethod;
import com.hankcs.hanlp.collection.trie.bintrie.BinTrie;
import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.io.IOException;
import java.util.Collection;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class BinTrieBasedSegmentation {
    public static void main(String[] args) throws IOException {
        // 加载字典
        TreeMap<String, CoreDictionary.Attribute> dictionary =
                IOUtil.loadDictionary("data/dictionary/CoreNatureDictionary.mini.txt");
        final BinTrie<CoreDictionary.Attribute> binTrie = new BinTrie<>(dictionary);
        Map<String, CoreDictionary.Attribute> binTrieMap = new Map<String, CoreDictionary.Attribute>() {
            @Override
            public int size() {
                return binTrie.size();
            }

            @Override
            public boolean isEmpty() {
                return binTrie.size() == 0;
            }

            @Override
            public boolean containsKey(Object key) {
                return binTrie.containsKey((String) key);
            }

            @Override
            public boolean containsValue(Object value) {
                throw new UnsupportedOperationException();
            }

            @Override
            public CoreDictionary.Attribute get(Object key) {
                return binTrie.get((String) key);
            }

            @Override
            public CoreDictionary.Attribute put(String key, CoreDictionary.Attribute value) {
                throw new UnsupportedOperationException();
            }

            @Override
            public CoreDictionary.Attribute remove(Object key) {
                throw new UnsupportedOperationException();
            }

            @Override
            public void putAll(Map<? extends String, ? extends CoreDictionary.Attribute> m) {
                throw new UnsupportedOperationException();
            }

            @Override
            public void clear() {
                throw new UnsupportedOperationException();
            }

            @Override
            public Set<String> keySet() {
                throw new UnsupportedOperationException();
            }

            @Override
            public Collection<CoreDictionary.Attribute> values() {
                throw new UnsupportedOperationException();
            }

            @Override
            public Set<Entry<String, CoreDictionary.Attribute>> entrySet() {
                throw new UnsupportedOperationException();
            }
        };

        String text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原";
        long start;
        double costTime;
        final int pressure = 10000;

        System.out.println("===相互接口===");

        System.out.println("完全切分");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            NaiveSegmentMethod.segmentFully(text, binTrieMap);
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f 万字/秒\n", text.length() * pressure / 10000 / costTime);

        System.out.println("===BinTrie接口===");

        System.out.println("完全切分");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            BinTrieSegmentMethod.segmentFully(text, binTrie);
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f 万字/秒\n", text.length() * pressure / 10000 / costTime);

        System.out.println("正向最长");
        start = System.currentTimeMillis();
        for (int i = 0; i < pressure; ++i)
            BinTrieSegmentMethod.segmentForwardLongest(text, binTrie);
        costTime = (System.currentTimeMillis() - start) / (double) 1000;
        System.out.printf("%.2f 万字/秒\n", text.length() * pressure / 10000 / costTime);

    }
}
