package ch02.sec06;

import com.hankcs.hanlp.algorithm.ahocorasick.trie.Emit;
import com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie;

import java.util.LinkedList;
import java.util.List;

public class AhoCorasickSegmentMethod {
    public static List<String> segmentFully(final String text, Trie dictionary) {
        final List<String> wordList=new LinkedList<>();
        for(Emit emit:dictionary.parseText(text))
            wordList.add(emit.getKeyword());
        return wordList;
    }
}
