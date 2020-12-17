package ch02.sec04;

import com.hankcs.hanlp.collection.trie.bintrie.BinTrie;
import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.util.LinkedList;
import java.util.List;

public class BinTrieSegmentMethod {
    public static List<String> segmentFully(final String text, BinTrie<CoreDictionary.Attribute> dictionary) {
        final List<String> wordList = new LinkedList<>();
        dictionary.parseText(text, (begin, end, attribute) -> wordList.add(text.substring(begin, end)));
        return wordList;
    }
    public static List<String> segmentForwardLongest(final String text, BinTrie<CoreDictionary.Attribute> dictionary){
        final List<String> wordList = new LinkedList<>();
        dictionary.parseLongestText(text, (begin, end, attribute) -> wordList.add(text.substring(begin,end)));
        return wordList;
    }
}

