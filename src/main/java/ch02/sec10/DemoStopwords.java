package ch02.sec10;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.collection.trie.DoubleArrayTrie;
import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.seg.Other.DoubleArrayTrieSegment;
import com.hankcs.hanlp.seg.Segment;
import com.hankcs.hanlp.seg.common.Term;
import org.jetbrains.annotations.NotNull;

import java.util.List;
import java.util.ListIterator;
import java.util.TreeMap;


public class DemoStopwords {
    public static void main(String[] args) {
        DoubleArrayTrie<String> trie = loadStopwordFromFile(HanLP.Config.CoreStopWordDictionaryPath);
        final String text = "停用词的意义相对而言无关紧要吧。";
        HanLP.Config.ShowTermNature = false;

        Segment segment = new DoubleArrayTrieSegment();
        List<Term> termList = segment.seg(text);
        System.out.println("分词结果：" + termList);

        removeStopwords(termList, trie);
        System.out.println("分词结果去掉停用词：" + termList);

        trie = loadStopwordFromWords("的", "相对而言", "吧");
        System.out.println("不分词去掉停用词：" + replaceStopwords(text, "**", trie));
    }

    private static @NotNull
    String replaceStopwords(final String text, final String replacement, DoubleArrayTrie<String> trie) {
        final StringBuilder stringBuilder = new StringBuilder(text.length());
        final int[] offset = new int[]{0};
        trie.parseLongestText(text, (begin, end, value) -> {
            if (begin > offset[0])
                stringBuilder.append(text, offset[0], begin);
            stringBuilder.append(replacement);
            offset[0] = end;
        });
        if (offset[0] < text.length())
            stringBuilder.append(text.substring(offset[0]));
        return stringBuilder.toString();
    }

    private static DoubleArrayTrie<String> loadStopwordFromWords(String... words) {
        TreeMap<String, String> map = new TreeMap<>();
        for (String word : words)
            map.put(word, word);
        return new DoubleArrayTrie<>(map);
    }

    private static void removeStopwords(List<Term> termList, DoubleArrayTrie<String> trie) {
        termList.removeIf(term -> trie.containsKey(term.word));
    }

    private static DoubleArrayTrie<String> loadStopwordFromFile(String path) {
        TreeMap<String, String> map = new TreeMap<>();
        IOUtil.LineIterator lineIterator = new IOUtil.LineIterator(path);
        for (String word : lineIterator)
            map.put(word, word);
        return new DoubleArrayTrie<>(map);
    }
}
