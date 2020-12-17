package ch02.sec05;

import com.hankcs.hanlp.collection.trie.DoubleArrayTrie;
import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.util.LinkedList;
import java.util.List;

public class DoubleArrayTrieSegmentMethod {
    public static List<String> segmentFully(final String text, DoubleArrayTrie<CoreDictionary.Attribute> dictionary) {
        final List<String> wordList = new LinkedList<>();
        dictionary.parseText(text, (begin, end, value) -> wordList.add(text.substring(begin, end)));
        return wordList;
    }

    public static List<String> segmentForwardLongest(final String text, DoubleArrayTrie<CoreDictionary.Attribute> dictionary){
        final List<String> wordList=new LinkedList<>();
        dictionary.parseLongestText(text,(begin, end, value) -> wordList.add(text.substring(begin,end)));
        return wordList;
    }
}
