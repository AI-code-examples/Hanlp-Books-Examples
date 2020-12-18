package ch02.sec02;

import com.hankcs.hanlp.dictionary.CoreDictionary;

import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class NaiveSegmentMethod {
    /**
     * 完全切分式的中文分词算法
     *
     * @param text       待分词的文本
     * @param dictionary 词典
     * @return 单词列表
     */
    public static List<String> segmentFully(String text, Map<String, CoreDictionary.Attribute> dictionary) {
        List<String> wordList = new LinkedList<String>();
        for (int i = 0; i < text.length(); ++i) {
            for (int j = i + 1; j <= text.length(); ++j) {
                String word = text.substring(i, j);
                if (dictionary.containsKey(word))
                    wordList.add(word);
            }
        }
        return wordList;
    }

    /**
     * 正向最长匹配的中文分词算法
     *
     * @param text       待分词的文本
     * @param dictionary 词典
     * @return 单词列表
     */
    public static List<String> segmentForwardLongest(String text, Map<String, CoreDictionary.Attribute> dictionary) {
        List<String> wordList = new LinkedList<String>();
        for (int i = 0; i < text.length(); ) {
            String longestWord = text.substring(i, i + 1);
            for (int j = i + 1; j <= text.length(); ++j) {
                String word = text.substring(i, j);
                if (dictionary.containsKey(word))
                    if (word.length() > longestWord.length())
                        longestWord = word;
            }
            wordList.add(longestWord);
            i += longestWord.length();
        }
        return wordList;
    }

    /**
     * 逆向最长匹配的中文分词算法
     *
     * @param text       待分词的文本
     * @param dictionary 词典
     * @return 单词列表
     */
    public static List<String> segmentBackwardLongest(String text, Map<String, CoreDictionary.Attribute> dictionary) {
        List<String> wordList = new LinkedList<String>();
        for (int i = text.length() - 1; i >= 0; ) {
            String longestWord = text.substring(i, i + 1);
            for (int j = 0; j <= i; ++j) {
                String word = text.substring(j, i + 1);
                if (dictionary.containsKey(word))
                    if (word.length() > longestWord.length()) {
                        longestWord = word;
                        break;
                    }
            }
            wordList.add(0, longestWord);
            i -= longestWord.length();
        }
        return wordList;
    }

    /**
     * 统计分词结果中的单字数量
     *
     * @param wordList 分词结果
     * @return 单字数量
     */
    public static int countSingleChar(List<String> wordList) {
        int size = 0;
        for (String word : wordList)
            if (word.length() == 1)
                ++size;
        return size;
    }

    /**
     * 双向最长匹配的中文分词算法
     *
     * @param text       待分词的文本
     * @param dictionary 词典
     * @return 单词列表
     */
    public static List<String> segmentBidirectional(String text, Map<String, CoreDictionary.Attribute> dictionary) {
        List<String> forwardLongest = segmentForwardLongest(text, dictionary);
        List<String> backwardLongest = segmentBackwardLongest(text, dictionary);
        if (forwardLongest.size() < backwardLongest.size())
            return forwardLongest;
        else if (forwardLongest.size() > backwardLongest.size())
            return backwardLongest;
        else {
            if (countSingleChar(forwardLongest) < countSingleChar(backwardLongest))
                return forwardLongest;
            else
                return backwardLongest;
        }
    }
}
